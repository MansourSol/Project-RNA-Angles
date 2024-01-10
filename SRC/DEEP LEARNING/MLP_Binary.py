import os
import glob
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
#train_data_folder = "../DATA MODIFIED/OneHotMatrices_OutputTrain/"
train_data_folder = "/Users/admin-21760/Desktop/M2/Computational Systems and Structural Biology/Bioinformatics of RNA and non-coding world/RNA_angles/RNA-project-angles/data/OneHotMatrices_OutputTrain/"
test_data_folder = "/Users/admin-21760/Desktop/M2/Computational Systems and Structural Biology/Bioinformatics of RNA and non-coding world/RNA_angles/RNA-project-angles/data/OneHotMatrices_OutputTest/"
train_labels_folder = "/Users/admin-21760/Desktop/M2/Computational Systems and Structural Biology/Bioinformatics of RNA and non-coding world/RNA_angles/RNA-project-angles/data/TrueAngles_TrainBINAIRE/"
test_labels_folder = "/Users/admin-21760/Desktop/M2/Computational Systems and Structural Biology/Bioinformatics of RNA and non-coding world/RNA_angles/RNA-project-angles/data/TrueAngles_TestBINAIRE/"

train_files = glob.glob(os.path.join(train_data_folder, "*.npy"))
test_files = glob.glob(os.path.join(test_data_folder, "*.npy"))

all_train_predictions = []
all_train_labels = []
all_test_predictions = []
all_test_labels = []

train_accuracy_history = []
test_accuracy_history = []
val_accuracy_history = []

for train_file, test_file in zip(train_files, test_files):
    train_label_file = os.path.join(train_labels_folder, os.path.basename(train_file).replace("_one_hot_matrix.npy", "_alpha.txt"))
    test_label_file = os.path.join(test_labels_folder, os.path.basename(test_file).replace("_one_hot_matrix.npy", "_alpha.txt"))

    train_x = np.load(train_file)
    train_y = np.loadtxt(train_label_file, dtype=int)

    test_x = np.load(test_file)
    test_y = np.loadtxt(test_label_file, dtype=int)

    train_x = train_x.reshape(train_x.shape[0], -1)
    test_x = test_x.reshape(test_x.shape[0], -1)
    train_x, val_x, train_y, val_y = train_test_split(train_x, train_y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    train_x = scaler.fit_transform(train_x)
    val_x = scaler.transform(val_x)
    test_x = scaler.transform(test_x)

    mlp_binary = MLPClassifier(hidden_layer_sizes=(100,), max_iter=500, random_state=42)

    train_accuracy_epoch = []
    test_accuracy_epoch = []
    val_accuracy_epoch = []

    for epoch in range(500):
        mlp_binary.partial_fit(train_x, train_y, classes=np.unique(train_y))
        train_loss = mlp_binary.loss_curve_

        train_accuracy = accuracy_score(train_y, mlp_binary.predict(train_x))
        train_accuracy_epoch.append(train_accuracy)

        val_accuracy = accuracy_score(val_y, mlp_binary.predict(val_x))
        val_accuracy_epoch.append(val_accuracy)
    
        test_accuracy = accuracy_score(test_y, mlp_binary.predict(test_x))
        test_accuracy_epoch.append(test_accuracy)
        test_loss = mlp_binary.loss_

    train_accuracy_history.append(train_accuracy_epoch)
    val_accuracy_history.append(val_accuracy_epoch)
    test_accuracy_history.append(test_accuracy_epoch)

for test_file in test_files:
    test_label_file = os.path.join(test_labels_folder, os.path.basename(test_file).replace("_one_hot_matrix.npy", "_alpha.txt"))
    protein_name = os.path.basename(test_file).replace("_one_hot_matrix.npy", "")

    test_x = np.load(test_file)
    test_x = test_x.reshape(test_x.shape[0], -1)
    test_x = scaler.transform(test_x)
    test_predictions = mlp_binary.predict(test_x)

    output_file = os.path.join("/Users/admin-21760/Desktop/M2/Computational Systems and Structural Biology/Bioinformatics of RNA and non-coding world/RNA_angles/RNA-project-angles/data/Y_pred_binary/", f"{protein_name}_predictions.txt")
    np.savetxt(output_file, test_predictions, fmt='%d')
    all_test_predictions.append(test_predictions)
    test_y = np.loadtxt(test_label_file, dtype=int)
    all_test_labels.append(test_y)

all_test_predictions = np.concatenate(all_test_predictions)
all_test_labels = np.concatenate(all_test_labels)
overall_test_accuracy = accuracy_score(all_test_labels, all_test_predictions)
print(f"Overall Test Accuracy: {overall_test_accuracy}")

plt.plot(train_loss, label='Training Loss')
plt.xlabel('Iterations')
plt.ylabel('Loss')
plt.legend()
plt.show()

plt.plot(np.mean(train_accuracy_history, axis=0), label='Training Accuracy')
plt.plot(np.mean(val_accuracy_history, axis=0), label='Validation Accuracy')
plt.plot(np.mean(test_accuracy_history, axis=0), label='Test Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()
