import os
import logging
class Config:
    
    API_ID = int(os.environ.get("API_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "Forward_BOT") 
    OWNER_ID = os.environ.get("OWNER_ID", "")
    DATABASE_URI = os.environ.get("DATABASE_URI", "")
    DATABASE_NAME = os.environ.get("DATABASE_NAME","Cluster0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Forward_data')
    SESSION = os.environ.get("SESSION", "AQBpcwnsTI_-uEJvfkBODpHo2P8EJoKLYI17M780GBHd6696aoZ7YxGNcl-QiMQhqPTOBUrFJ-SEGFfQ7pbZoS0d_lepj-uTK2aFGIPwK5yqvNVsrWodkfGv0JU8WqjpO8hVTQyuY_KK4cHa5FMOk_bZDNeCjtXsGfd6IZxfYW76NGM5QpbxLxZYd_yPRz0AzjJeNPZqkubJ3dWDfwxARNLop3k9pImNdKEsHMNw4NnFg8UJfgRA-5oYJWL6vKMXbCo5xHYsPKmB6Qs2eTH-KGEmIuotHmnAvMBslRXfkvVvysk83GUOoFq2lqpEwBbEEmzndIuClrky2vqRV9lj1_YFQbZa9QA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", ""))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", None)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
