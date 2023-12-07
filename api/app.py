from flask import Flask, jsonify, request
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from models.episode import Episode
from models.color import Color
from models.subject_matter import SubjectMatter
import os

app = Flask(__name__)

# Database setup
username = os.getenv('MYSQL_USERNAME', 'root')
password = os.getenv('MYSQL_PASSWORD', '')
host = os.getenv('MYSQL_HOST', 'localhost')
db_name = os.getenv('MYSQL_DB_NAME', 'JoyOfPaintingDB')
engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@{host}/{db_name}')
Session = sessionmaker(bind=engine)

@app.route('/api/episodes', methods=['GET'])
def get_episodes():
    session = Session()

    # Start with a query on the Episode model
    query = session.query(Episode)

    # Filter by month
    month = request.args.get('month')
    if month:
        query = query.filter(func.month(Episode.AirDate) == func.month(func.str_to_date(month, '%M')))

    # Filter by subject matter
    subject = request.args.get('subject')
    if subject:
        query = query.join(Episode.subject_matters).filter(SubjectMatter.SubjectName == subject)

    # Filter by color
    color = request.args.get('color')
    if color:
        query = query.join(Episode.colors).filter(Color.ColorName == color)

    episodes = query.all()
    session.close()

    episodes_list = [{'title': ep.Title, 'air_date': ep.AirDate.strftime('%Y-%m-%d')} for ep in episodes]
    return jsonify({'episodes': episodes_list})

if __name__ == '__main__':
    app.run(debug=True)
