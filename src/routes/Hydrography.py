from flask import Blueprint, jsonify, request
import uuid

# Entities
from models.entities.Hydrography import SubCatchment, Well
# Models
from models.HydrographyModel import HydrographyModel

main = Blueprint('subcatchment_blueprint', __name__)


@main.route('/subcatchments')
def get_subcatchments():
    try:
        subcatchments = HydrographyModel.get_subcatchments()
        return jsonify(subcatchments)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/subcatchment/<id>')
def get_subcatchment(id):
    try:
        subcatchment = HydrographyModel.get_subcatchment(id)
        if subcatchment != None:
            return jsonify(subcatchment)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/subcatchment/add', methods=['POST'])
def add_subcatchment():
    
    try:
        
        id = request.json['id']
        Nombre = request.json['Nombre']
        Area_km2 = request.json['Area_km2']
        par_a = request.json['par_a']
        par_tau = request.json['par_tau']
        par_p0 = request.json['par_p0']
        par_lan = request.json['par_lan']
        par_fcp = request.json['par_fcp']
        par_ks = request.json['par_ks']
        par_tc1 = request.json['par_tc1']
        par_tc2 = request.json['par_tc2']
        Qthr_1 = request.json['Qthr_1']
        Qthr_2 = request.json['Qthr_2']
        Qthr_3 = request.json['Qthr_3']
        
        subcatchment = SubCatchment(id, Nombre, Area_km2, par_a,par_tau, par_p0, par_lan, par_fcp, par_ks,par_tc1,par_tc2, Qthr_1,Qthr_2, Qthr_3)
        
        affected_rows = HydrographyModel.add_subcatchment(subcatchment)
        
        if affected_rows == 1:
            return jsonify(subcatchment.id)
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        
        return jsonify({'message': str(ex)}), 500



@main.route('/subcatchment/update/<id>', methods=['PUT'])
def update_subcatchment(id):
    try:
        Nombre = request.json['Nombre']
        Area_km2 = request.json['Area_km2']
        par_a = request.json['par_a']
        par_tau = request.json['par_tau']
        par_p0 = request.json['par_p0']
        par_lan = request.json['par_lan']
        par_fcp = request.json['par_fcp']
        par_ks = request.json['par_ks']
        par_tc1 = request.json['par_tc1']
        par_tc2 = request.json['par_tc2']
        Qthr_1 = request.json['Qthr_1']
        Qthr_2 = request.json['Qthr_2']
        Qthr_3 = request.json['Qthr_3']

        subcatchment = SubCatchment(id, Nombre, Area_km2, par_a,par_tau, par_p0, par_lan, par_fcp, par_ks,par_tc1,par_tc2, Qthr_1,Qthr_2, Qthr_3)

        affected_rows = HydrographyModel.update_subcatchment(subcatchment)

        if affected_rows == 1:
            return jsonify(subcatchment.id)
        else:
            return jsonify({'message': "No subcatchment updated"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/subcatchment/delete/<id>', methods=['DELETE'])
def delete_subcatchment(id):
    try:
        subcatchment = SubCatchment(id)

        affected_rows = HydrographyModel.delete_subcatchment(subcatchment)

        if affected_rows == 1:
            return jsonify(subcatchment.id)
        else:
            return jsonify({'message': "No subcatchment deleted"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

#_________________________________________________________________________
#---------------------     WELLS       -----------------------------------
#_________________________________________________________________________

@main.route('/wells')
def get_wells():
    try:
        wells = HydrographyModel.get_wells()
        return jsonify(wells)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/well/<id>')
def get_well(id):
    try:
        well = HydrographyModel.get_well(id)
        if well != None:
            return jsonify(well)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/well/add', methods=['POST'])
def add_well():
    
    try:
        
        id = request.json['id']
        Annual = request.json['Annual']
        Spring = request.json['Spring']
        Summer = request.json['Summer']
        Winter = request.json['Winter']
        Autumn = request.json['Autumn']
        
        well = Well(id,  Annual, Spring, Summer,Winter, Autumn)
        
        affected_rows = HydrographyModel.add_well(well)
        
        if affected_rows == 1:
            return jsonify(well.id)
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        
        return jsonify({'message': str(ex)}), 500

@main.route('/well/update/<id>', methods=['PUT'])
def update_well(id):
    try:
        Annual = request.json['Annual']
        Spring = request.json['Spring']
        Summer = request.json['Summer']
        Winter = request.json['Winter']
        Autumn = request.json['Autumn']

        well = Well(id, Annual, Spring, Summer,Winter, Autumn)
        
        affected_rows = HydrographyModel.update_well(well)

        if affected_rows == 1:
            return jsonify(well.id)
        else:
            return jsonify({'message': "No subcatchment updated"}), 404

    except Exception as ex:
        
        return jsonify({'message': str(ex)}), 500

@main.route('/well/delete/<id>', methods=['DELETE'])
def delete_well(id):
    
    try:
        well = Well(id)

        affected_rows = HydrographyModel.delete_well(well)
        
        if affected_rows == 1:
            return jsonify(well.id)
        else:
            return jsonify({'message': "No subcatchment deleted"}), 404

    except Exception as ex:
        
        return jsonify({'message': str(ex)}), 500