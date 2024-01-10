import os
def calculate_mean(values):
    return sum(values) / len(values)

alpha_folder = "Y_pred_binary"
reverse_folder = "Reverse_TestBinaireYPRED"

mean_folder = "MeanBinary"
for filename_alpha in os.listdir(alpha_folder):
    if filename_alpha.endswith("_predictions.txt"):
        path_alpha = os.path.join(alpha_folder, filename_alpha)
        filename_reverse = filename_alpha.replace("_predictions.txt", "_predictions.txt")
        path_reverse = os.path.join(reverse_folder, filename_reverse)
        if os.path.exists(path_reverse):
            with open(path_alpha, 'r') as file_alpha:
                alpha_values = [float(line.strip()) for line in file_alpha.readlines()]
            with open(path_reverse, 'r') as file_reverse:
                reverse_values = [float(line.strip()) for line in file_reverse.readlines()]
            differences = [a - b for a, b in zip(alpha_values, reverse_values)]
            mean = calculate_mean(differences)
            output_path = os.path.join(mean_folder, filename_alpha.replace("_predictions.txt", "_mean.txt"))
            with open(output_path, 'w') as output_file:
                output_file.write(str(mean))

average_means = []

for filename_mean in os.listdir(mean_folder):
    if filename_mean.endswith("_mean.txt"):
        path_mean = os.path.join(mean_folder, filename_mean)
        with open(path_mean, 'r') as file_mean:
            mean_value = float(file_mean.read())
        average_means.append(mean_value)
overall_average = calculate_mean(average_means)
print(f"Moyenne globale des moyennes : {overall_average}")
mean_total_path = os.path.join(os.getcwd(), "mean_total.txt")
with open(mean_total_path, 'w') as mean_total_file:
    mean_total_file.write(str(overall_average))

print(f"Moyenne globale des moyennes : {overall_average}")
