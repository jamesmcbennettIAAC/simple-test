import compute_rhino3d.Util
import compute_rhino3d.Grasshopper as gh
import rhino3dm
import json

compute_rhino3d.Util.url = "http://localhost:8081/"
#compute_rhino3d.Util.apiKey = ""

defName = 'assets/simple.gh'
file_path = 'assets/simple.json'


try:
    with open(file_path, 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    print(f'The file {file_path} was not found.')

except json.JSONDecodeError:
    print(f'Error decoding JSON from {file_path}.')


#from simple.json
try:
    #typology = data['properties']['typology']
    typology = "c"
    print(typology)
    typology_tree = gh.DataTree('RH_IN:typology')
    typology_tree.Append([0], [typology])

except Exception as e:
    print(f'Error constructing DataTree: {e}.')


trees = [typology_tree]
print(trees)

#from Grasshopper
try:
    output = gh.EvaluateDefinition(defName, trees)
    #print(output)

    points_data = output['values'][0]['InnerTree']['{0;0}']
    xyz_points = []

    for points in points_data:
        point = json.loads(points['data'])
        xyz_points.append([point['X'], point['Y'], point['Z']])

    print(xyz_points)

except Exception as e:
    print(f'Error running grasshopper file: {e}.')

if output:
    # writing JSON data
    with open("assets/simple-output.json", 'w') as f:
        json.dump(xyz_points, f)
