from config.cities_continent import tier1_country,tier2_country,tier3_country,Africa,Asia,Oceania,Europe,North_America,South_America
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal

class UserInput(BaseModel):
    quantity:Annotated[float,Field(...,lt=60000,description='Enter the quantity you want to export(less than 60k)',examples=[5400])]
    drawback:Annotated[float,Field(...,lt=314727,description='Enter the drawback(less than 314K)',examples=[54000.5])]
    foreign_country:Annotated[str,Field(...,description='Enter the place of export',examples=['Russia'])]
    categories:Annotated[Literal['Glazed Vitrified Tiles','Glazed Porcelain Tiles','Ceramic Wall Tiles','Ceramic Floor Tiles','Polished Glazed Vitrified Tiles','Others Commodities'],Field(...,description='Enter the category of you product',examples=['Polished Glazed Vitrified Tiles'])]
    # 'QTY', 'DRAWBACK'-'numbers', 'FOREIGN_COUNTRY'-'numbers', 'Categories'-'numbers','FOREIGN PORT CONTINENT'-'numbers'
    
    @computed_field
    @property
    def drawback_num(self)->int:
        if self.quantity<2818.5:
            return 0
        elif self.quantity<5432.5:
            return 1
        elif self.quantity<11099.75:
            return 2
        else:
            return 3
    
    @computed_field
    @property
    def foreign_country_num(self)->int:
        if self.foreign_country in tier1_country:
            return 1
        elif self.foreign_country in tier2_country:
            return 2 
        else:
            return 3
    
    @computed_field
    @property
    def categories_num(self)->int:
        if self.categories =='Glazed Vitrified Tiles':
            return 1
        elif self.categories =='Glazed Porcelain Tiles':
            return 2
        elif self.categories =='Others Commodities':
            return 3
        elif self.categories =='Ceramic Wall Tiles':
            return 4
        elif self.categories =='Ceramic Floor Tiles':
            return 5
        elif self.categories =='Polished Glazed Vitrified Tiles':
            return 6
        else:
            return 7
    
    @computed_field
    @property
    def FOREIGN_PORT_CONTINENT(self)->int:
        if self.foreign_country in Asia:
            return 1
        elif self.foreign_country in Europe:
            return 2
        elif self.foreign_country in North_America:
            return 3
        elif self.foreign_country in Africa:
            return 4
        elif self.foreign_country in South_America:
            return 5
        else:
            return 6