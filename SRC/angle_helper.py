import os
import json

class AngleHelper:
  def __init__(self, *args, **kwargs):
    # TO BE COMPLETE
    pass


  def predict(self, in_path_seq: str, in_path_ang: str, out_path: str):

    sequences = {}
    with open(in_path_seq, 'r') as fasta_file:
        lines = fasta_file.readlines()
        for i in range(0, len(lines), 2):
            sequence_name = lines[i][1:].strip()
            sequence = lines[i + 1].strip()
            sequences[sequence_name] = sequence

    with open(in_path_ang, 'r') as angles_file:
        angles = [float(line.strip()) for line in angles_file if float(line.strip()) != 0.0]

    sequence_name, sequence = sequences.popitem()

    data = {
        sequence_name: {
            "sequence": sequence,
            "angles": {"alpha": angles}
        }
    }
    with open(out_path, 'w') as json_file:
        json.dump(data, json_file, indent=2)



    return None

if __name__ == "__main__":
    # Example of usage
    in_path_seq = "../DATA/sample/example.fasta"
    in_path_ang = "../RESULTS/PREDICTION_SAMPLE/Reverse_TestBinaireExample/example_pred.txt"
    out_path = "../RESULTS/sample.json"
    angle_helper = AngleHelper()
    angle_helper.predict(in_path_seq, in_path_ang, out_path)

