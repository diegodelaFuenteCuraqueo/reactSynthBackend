from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS
from config import config

app = Flask(__name__)
CORS(app)
connection = MySQL(app)

@app.route('/synth-presets')
def synth_presets():
  try:
    cursor = connection.connection.cursor()
    cursor.execute('SELECT name, modulation_index, harmonicity, low_key, number_of_keys FROM tbl_FM_presets')
    datos = cursor.fetchall()
    presets = []
    for dato in datos:
      preset={ 'name': dato[0], 'modulation_index': dato[1], 'harmonicity': dato[2], 'low_key': dato[3], 'number_of_keys': dato[4] }
      presets.append(preset)
    print(preset)
    return jsonify({ 'presets': presets})
  except Exception as e:
    return jsonify({ 'error': str(e) })

@app.route('/synth-presets/<id>')
def getPreset(id):
  try:
    cursor = connection.connection.cursor()
    cursor.execute('SELECT name, modulation_index, harmonicity, low_key, number_of_keys FROM tbl_FM_presets WHERE id=%s', (id))
    dato = cursor.fetchone()
    preset={ 'name': dato[0], 'modulation_index': dato[1], 'harmonicity': dato[2], 'low_key': dato[3], 'number_of_keys': dato[4] }
    return jsonify({ 'preset': preset})
  except Exception as e:
    return jsonify({ 'error': str(e) })

#@app.route('/synth-presets/name/<name>')
#def getPresetByName(name):
#  try:
#    cursor = connection.connection.cursor()
#    cursor.execute('SELECT name, modulation_index, harmonicity, low_key, number_of_keys FROM tbl_FM_presets WHERE name=%s', (name))
#    dato = cursor.fetchone()
#    preset={ 'name': dato[0], 'modulation_index': dato[1], 'harmonicity': dato[2], 'low_key': dato[3], 'number_of_keys': dato[4] }
#    return jsonify({ 'preset': preset})
#  except Exception as e:
#    return jsonify({ 'error': str(e) })

@app.route('/synth-presets', methods=['POST'])
def addPreset():
  try:
    cursor = connection.connection.cursor()
    cursor.execute('INSERT INTO tbl_FM_presets (name, modulation_index, harmonicity, low_key, number_of_keys) VALUES (%s, %s, %s, %s, %s)', (request.json['name'], request.json['modulation_index'], request.json['harmonicity'], request.json['low_key'], request.json['number_of_keys']))
    connection.connection.commit()
    return jsonify({ 'message': 'Preset added successfully' })
  except Exception as e:
    return jsonify({ 'error': str(e) })

@app.route('/synth-presets/<id>', methods=['PUT'])
def updatePreset(id):
  try:
    cursor = connection.connection.cursor()
    cursor.execute('UPDATE tbl_FM_presets SET name=%s, modulation_index=%s, harmonicity=%s, low_key=%s, number_of_keys=%s WHERE id=%s', (request.json['name'], request.json['modulation_index'], request.json['harmonicity'], request.json['low_key'], request.json['number_of_keys'], id))
    connection.connection.commit()
    return jsonify({ 'message': 'Preset updated successfully' })
  except Exception as e:
    return jsonify({ 'error': str(e) })

@app.route('/synth-presets/<id>', methods=['DELETE'])
def deletePreset(id):
  try:
    cursor = connection.connection.cursor()
    cursor.execute('DELETE FROM tbl_FM_presets WHERE id=%s', (id))
    connection.connection.commit()
    return jsonify({ 'message': 'Preset deleted successfully' })
  except Exception as e:
    return jsonify({ 'error': str(e) })

def notFound(error):
  return '<h1>not found (404)</h1>'

if __name__ == '__main__':
  app.config.from_object(config['development'])
  app.register_error_handler(404, notFound)
  app.run()