from pydantic import Field, BaseModel, BaseConfig


class ProductSchema(BaseModel):
    title: str = Field(...)
    author: str = Field(...)
    publisher: str = Field(...)
    edition: str = Field(...)
    description: str = Field(...)
    regular_price: int = Field(...)
    sell_price: int = Field(...)
    language: str = Field(...)
    genre: list[str] = Field(...)
    category: str = Field(...)
    sub_category: str = Field(default=None)
      
    
    class Config(BaseConfig):
        schema_extra = {
            "example": {
                'title': 'lilabotir mrittu',
                'author': 'humayun ahmed',
                'publisher': 'anonna publisher',
                'edition': '1990, 4th Edition',
                'description': 'Good book',
                'regular_price': 500,
                'sell_price': 450,
                'language': 'bn',
                'genre': ['thriller', 'history'],
                'category': 'Humayun ahmed',
                'sub_category': 'Novel',
            }
        }