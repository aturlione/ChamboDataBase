from database.db import get_connection
from .entities.Hydrography import SubCatchment, Well


class HydrographyModel():

    @classmethod
    def get_subcatchments(self):
        
        try:
            connection = get_connection()
            subcatchments = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM sub_catchments ORDER BY id ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    subcatchment = SubCatchment(row[0], row[1], row[2], row[3],row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13] )
                    subcatchments.append(subcatchment.to_JSON())

            connection.close()
            return subcatchments
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_subcatchment(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM sub_catchments WHERE id = %s", (id,))
                row = cursor.fetchone()

                subcatchment = None
                if row != None:
                    subcatchment = SubCatchment(row[0], row[1], row[2], row[3],row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13] )
                    subcatchment = subcatchment.to_JSON()

            connection.close()
            return subcatchment
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_subcatchment(self, subcatchment):
        
        try:
            connection = get_connection()
            

            with connection.cursor() as cursor:
                
                cursor.execute("""INSERT INTO sub_catchments (id,"Nombre", "Area_km2", par_a, par_tau, par_p0, par_lan, par_fcp, par_ks, par_tc1, par_tc2, "Qthr_1", "Qthr_2", "Qthr_3") 
                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (subcatchment.id, subcatchment.Nombre, subcatchment.Area_km2, subcatchment.par_a,subcatchment.par_tau, subcatchment.par_p0, subcatchment.par_lan, subcatchment.par_fcp, subcatchment.par_ks, subcatchment.par_tc1, subcatchment.par_tc2, subcatchment.Qthr_1, subcatchment.Qthr_2, subcatchment.Qthr_3))
                
                affected_rows = cursor.rowcount
        
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
           
            raise Exception(ex)



    @classmethod
    def update_subcatchment(self, subcatchment):
        
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE sub_catchments SET "Nombre" = %s, "Area_km2" = %s, par_a = %s , par_tau = %s, par_p0 = %s, par_lan = %s, par_fcp = %s, par_ks = %s, par_tc1 = %s, par_tc2 = %s, "Qthr_1" = %s, "Qthr_2" = %s, "Qthr_3" = %s
                                WHERE id = %s""", (  subcatchment.Nombre, subcatchment.Area_km2, subcatchment.par_a,subcatchment.par_tau, subcatchment.par_p0, subcatchment.par_lan, subcatchment.par_fcp, subcatchment.par_ks, subcatchment.par_tc1, subcatchment.par_tc2, subcatchment.Qthr_1, subcatchment.Qthr_2, subcatchment.Qthr_3,subcatchment.id))
                
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            
            raise Exception(ex)

    @classmethod
    def delete_subcatchment(self, subcatchment):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM sub_catchments WHERE id = %s", (subcatchment.id,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
#_________________________________________________________________________
#---------------------     WELLS       -----------------------------------
#_________________________________________________________________________
    @classmethod
    def get_wells(self):
        
        try:
            connection = get_connection()
            wells = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM wells ORDER BY id ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    well = Well(row[0], row[1], row[2], row[3],row[4],row[5] )
                    wells.append(well.to_JSON())

            connection.close()
            return wells
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_well(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM wells WHERE id = %s", (id,))
                row = cursor.fetchone()

                subcatchment = None
                if row != None:
                    well = Well(row[0], row[1], row[2], row[3],row[4],row[5]  )
                    well = well.to_JSON()

            connection.close()
            return well
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_well(self, well):
        
        try:
            connection = get_connection()
            

            with connection.cursor() as cursor:
                
                cursor.execute("""INSERT INTO wells (id,  "Annual", "Spring", "Summer", "Winter", "Autumn") 
                                    VALUES (%s, %s, %s, %s, %s, %s)""", (well.id,well.Annual,well.Spring,well.Summer,well.Winter,well.Autumn))
                
                affected_rows = cursor.rowcount
        
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
           
            raise Exception(ex)

    @classmethod
    def update_well(self, well):
        
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE wells SET   "Annual" = %s, "Spring" = %s, "Summer" = %s , "Winter" = %s, "Autumn" = %s
                                WHERE id = %s""", (   well.Annual, well.Spring,well.Summer, well.Winter, well.Autumn,well.id))
                
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            
            raise Exception(ex)

    @classmethod
    def delete_well(self, well):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM wells WHERE id = %s", (well.id,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            
            return affected_rows
        except Exception as ex:
            print('lalala')
            raise Exception(ex)