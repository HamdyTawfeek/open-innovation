import pandas as pd
from sqlalchemy.engine.base import Engine
from app.db import engine


def resize_frames(path: str) -> pd.DataFrame:
    images_df = pd.read_csv(path)
    depth = images_df['depth']
    img_data = images_df.drop('depth', axis = 1)
    images_scaled_df = img_data.sample(n=150, axis=1)
    images_scaled_df.insert(0, 'depth', depth)
    return images_scaled_df

def apply_color_map(df: pd.DataFrame) -> pd.DataFrame:
    # TODO apply the color map
    df_colored = df
    return df_colored

def write_frames_to_db(df: pd.DataFrame, conn:Engine,  table: str):
    df.to_sql(table, con=conn, if_exists='replace', index=False)

def adjust_and_store_frames():
    df_scaled = resize_frames('./app/resources/img.csv')
    df_colored = apply_color_map(df_scaled)
    write_frames_to_db(df_colored, engine, 'data')
