
import CONFIG

from motor.motor_asyncio import AsyncIOMotorClient
client = AsyncIOMotorClient(CONFIG.MONGODB_URI)
db = client.neuralflow