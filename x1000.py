import compute_rhino3d.Util
import compute_rhino3d.Grasshopper as gh
import rhino3dm
import json

compute_rhino3d.Util.url = "http://localhost:8081/"

defName = 'assets/x1000.gh'

try:
    #integer = 6
    integer = int(input("Enter an integer: "))
    int_tree = gh.DataTree('RH_IN:integer')
    int_tree.Append([0], [integer])

except Exception as e:
    print(f'Error constructing DataTree: {e}.')

trees = [int_tree]

try:
    output = gh.EvaluateDefinition(defName, trees)

    # Extract the value from the output
    result = int(output['values'][0]['InnerTree']['{0}'][0]['data'].strip('"'))

    print(result)

except Exception as e:
    print(f'Error running grasshopper file: {e}.')