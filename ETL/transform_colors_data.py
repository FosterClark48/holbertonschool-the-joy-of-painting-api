import pandas as pd
import re

# Function to standardize episode titles
def standardize_title(title):
    # Initial standardization
    title = title.replace('Mt.', 'Mount').replace('"', '').strip()
    title = title.title()  # Convert to title case

    # Specific replacements
    special_cases = {
        "Quiet Mountains River": "Quiet Mountain River",
        "The Footbridge": "Footbridge",
        "Forest Down Oval": "Forest Dawn Oval",
        "Storm'S A Comin": "Storm's A Comin'",
        "Gray Mountain": "Grey Mountain",
        "Cabin At Trails End": "Cabin At Trail's End",
        "The Old Oak Tree": "Old Oak Tree",
        "Summer In The Mountain": "Summer In The Mountains",
        "Rivers Peace": "River's Peace",
        "Mountain Path": "Mountain Pass",
        "Snow Fall": "Snowfall",
        "Half-Oval Vignette": "Half Oval Vignette",
        "Winter In Pastel": "Pastel Winter",
        "Black And White Seascape": "Black & White Seascape",
        "The Old Home Place": "Old Home Place",
        "Shades Of Grey": "Shades Of Gray",
        "Hide A Way Cove": "Hide-A-Way Cove",
        "Evening At Sunset": "Evening Sunset",
        "Autumn Mountain": "Autumn Mountains",
        "Golden Rays Of Sunshine": "Golden Rays Of Sunlight",
        "Toward Days End": "Toward Day's End",
        "Evergreens At Sunset": "Evergreen At Sunset",
        "A Pretty Autumn Day": "Pretty Autumn Day",
        "Misty Forest Oval": "Misty Forest",
        # Add more specific cases here
    }

    # Check if the title matches any special case
    for key, value in special_cases.items():
        if key.lower() == title.lower():
            return value

    # General handling for 's at the end of words
    title = re.sub(r"(\w)'S(\s|$)", r"\1's\2", title)

    return title

# Load the dataset
colors_used_path = 'Datasets/The Joy Of Painiting - Colors Used'
colors_used_df = pd.read_csv(colors_used_path)

# Standardize and clean episode titles
colors_used_df['painting_title'] = colors_used_df['painting_title'].apply(standardize_title)

# Clean and extract unique colors
unique_colors = set()
for color_list in colors_used_df['colors']:
    colors = eval(color_list)
    cleaned_colors = [re.sub(r'[\r\n]+', '', color).strip() for color in colors]
    unique_colors.update(cleaned_colors)

# DataFrame for Colors Table
colors_df = pd.DataFrame({'ColorName': list(unique_colors)})

# DataFrame for EpisodeColors Junction Table
episode_colors_data = []
for _, row in colors_used_df.iterrows():
    episode_id = f"S{str(row['season']).zfill(2)}E{str(row['episode']).zfill(2)}"
    colors = eval(row['colors'])
    cleaned_colors = [re.sub(r'[\r\n]+', '', color).strip() for color in colors]
    for color in cleaned_colors:
        episode_colors_data.append({'EpisodeID': episode_id, 'ColorName': color})

episode_colors_df = pd.DataFrame(episode_colors_data)

# Save the DataFrames to CSV files
colors_df.to_csv('ETL/transformed_colors.csv', index=False)
episode_colors_df.to_csv('ETL/transformed_episode_colors.csv', index=False)

print("DataFrames saved as CSV files in the ETL directory.")
