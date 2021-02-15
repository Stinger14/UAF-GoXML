"""
    Projecto: UAF goXML generator app
    Descripción: Aplicación web de pequeña escala para la generación de archivos XML requeridos por la UAF.
    Desarrollador: Maxly García
"""

import pathlib
from flask import Flask
from .uafxml3 import RteXml
from .resources import get_resources_path

BASE_DIR = pathlib.Path(__file__).resolve().parent
DATA_DIR = get_resources_path("data")
TEMPLATE = get_resources_path("data/_Web_Report_ReportID_3234-0-0.xml")
WORKBOOK = get_resources_path("data/transacciones_efectivo_2019_alt.xlsx")
RTEMAP = get_resources_path("data/mapped_elements.xlsx")

web_app = Flask(__name__)

@web_app.route('/', methods=['GET'])    #http://localhost:5002/
def index():
    return {'template_dir': str(TEMPLATE)}, 200

@web_app.route('/generate_xml', methods=['GET', 'POST'])    #http://localhost:5002/generate_xml
def gen_xml():

    #TODO 1) Generate tree from xml file
    xml_template = RteXml(TEMPLATE, WORKBOOK, RTEMAP)
    # tree = xml_template._get_tree()
    # print(f'Tree: {tree}')
    
    #TODO 2) Create dict with RTE Excel column names
    xml_template._get_rte_keys()

    #TODO 3) Create dict with XML element names
    xml_template._get_xml_elements()

    # TODO 4) Update xml file with dict updated values
    adict = xml_template.get_rteuaf_dict()
    
    # TODO 5) Save updated xml
    xml_template._update_xml(adict)

    return {'XML': adict}, 200

    # xml = dicttoxml(adict)
    # xml_decode = xml.decode()

    # xml.writexml(open("report_updated", "w"))
    # xmlfile = open("report_updated.xml", "w")

    # xmlfile.write(adict)
    # xmlfile.close()
    
    # xml_template.save_xml(domtree)
    # return {'xml_values': adict}, 200
