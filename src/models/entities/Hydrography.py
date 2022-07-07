from utils.DateFormat import DateFormat


class SubCatchment():  

    def __init__(self,id,Nombre=None,Area_km2=None,par_a=None, par_tau=None, par_p0=None, par_lan=None, par_fcp=None, par_ks=None, par_tc1=None, par_tc2=None, Qthr_1=None, Qthr_2=None, Qthr_3=None) -> None:
        self.id=id
        self.Nombre=Nombre
        self.Area_km2=Area_km2
        self.par_a=par_a
        self.par_tau=par_tau
        self.par_p0=par_p0
        self.par_lan=par_lan
        self.par_fcp=par_fcp
        self.par_ks=par_ks
        self.par_tc1=par_tc1
        self.par_tc2=par_tc2
        self.Qthr_1=Qthr_1
        self.Qthr_2=Qthr_2
        self.Qthr_3=Qthr_3
    def to_JSON(self):
        return{
            'id':self.id,
            'Nombre':self.Nombre,
            'Area_km2':self.Area_km2,
            'par_a':self.par_a,
            'par_tau':self.par_tau,
            'par_p0':self.par_p0,
            'par_lan':self.par_lan,
            'par_fcp':self.par_fcp,
            'par_ks':self.par_ks,
            'par_tc1':self.par_tc1,
            'par_tc2':self.par_tc2,
            'Qthr_1':self.Qthr_1,
            'Qthr_2':self.Qthr_2,
            'Qthr_3':self.Qthr_3
        }

class Well():  

    def __init__(self,id,Annual=None,Spring=None,Summer=None, Winter=None, Autumn=None) -> None:
        self.id=id
        self.Annual=Annual
        self.Spring=Spring
        self.Summer=Summer
        self.Winter=Winter
        self.Autumn=Autumn
    def to_JSON(self):
        return{
            'id':self.id,
            'Annual':self.Annual,
            'Spring':self.Spring,
            'Summer':self.Summer,
            'Winter':self.Winter,
            'Autumn':self.Autumn,
        }