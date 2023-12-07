import pandas as pd
import os
import sys
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database credentials
USERNAME = os.getenv('MYSQL_USERNAME', 'root')
PASSWORD = os.getenv('MYSQL_PASSWORD', '')
HOST = os.getenv('MYSQL_HOST', 'localhost')
DB_NAME = os.getenv('MYSQL_DB_NAME', 'JoyOfPaintingDB')

# SQLAlchemy setup
engine = create_engine(f'mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{HOST}/{DB_NAME}')
Session = sessionmaker(bind=engine)
session = Session()

# Define table models
metadata = MetaData()
colors = Table('Colors', metadata, autoload_with=engine)
episode_colors = Table('EpisodeColors', metadata, autoload_with=engine)

# Load transformed data
colors_df = pd.read_csv('ETL/transformed_colors.csv')
episode_colors_df = pd.read_csv('ETL/transformed_episode_colors.csv')

# Retrieve existing colors from the database
existing_colors = pd.read_sql('SELECT ColorName FROM Colors', engine)['ColorName'].tolist()

# Insert Colors data and retrieve ColorName to ColorID mapping
color_id_map = {}
try:
    for _, row in colors_df.iterrows():
        color_name = row['ColorName']
        if color_name not in existing_colors:  # Check if color already exists
            ins = colors.insert().values(ColorName=color_name)
            result = session.execute(ins)
            color_id = result.inserted_primary_key[0]
        else:  # If color exists, get its ColorID
            color_id = session.execute(select(colors.c.ColorID).where(colors.c.ColorName == color_name)).scalar()
        color_id_map[color_name] = color_id
    session.commit()
except Exception as e:
    print(f"Error loading Colors data: {e}", file=sys.stderr)
    session.rollback()

# Insert EpisodeColors data
try:
    for _, row in episode_colors_df.iterrows():
        color_id = color_id_map.get(row['ColorName'])
        if color_id:
            ins = episode_colors.insert().values(EpisodeID=row['EpisodeID'], ColorID=color_id)
            session.execute(ins)
    session.commit()
except Exception as e:
    print(f"Error loading EpisodeColors data: {e}", file=sys.stderr)
    session.rollback()

session.close()
print("Data loaded into Colors and EpisodeColors tables.")
