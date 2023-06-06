from decouple import config
import motor.motor_asyncio


MONGODB_URI = config('MONGODB_URI')

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URI)
db = client.test_database
