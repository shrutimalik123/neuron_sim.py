import math
import random

def neural_network_game():
    # 1. Scenario: Digit Recognition
    # Input: A pixel intensity value (0 to 1)
    print("--- 🧠 THE HIDDEN LAYER: NEURON SIM 🧠 ---")
    print("Mission: Guide a signal through a single neuron to classify a digit.")
    print("Goal: Adjust the Weight and Bias to trigger the 'Activation Function'.")

    # 2. Input Data
    pixel_intensity = 0.8  # Representing a dark pixel of a '1'
    print(f"\nIncoming Pixel Signal: {pixel_intensity}")

    # 3. Hyperparameters: Weight and Bias
    print("\n--- STEP 1: CONFIGURE THE SYNAPSE ---")
    print("Weight: How much importance to give this pixel.")
    print("Bias: The threshold to overcome before the neuron fires.")
    
    try:
        weight = float(input("Enter Weight (e.g., 2.0): "))
        bias = float(input("Enter Bias (e.g., -1.0): "))
    except ValueError:
        weight, bias = 1.0, 0.0

    # 4. The Math: Weighted Sum & Activation
    # Formula: Activation( (Input * Weight) + Bias )
    weighted_sum = (pixel_intensity * weight) + bias
    
    # Using the ReLU (Rectified Linear Unit) Activation Function
    # Formula: max(0, x)
    output = max(0, weighted_sum)

    print(f"\n--- 🖥️ NEURON PROCESSING... ---")
    print(f"Weighted Sum: {weighted_sum:.2f}")
    print(f"Neuron Output (ReLU): {output:.2f}")

    # 5. Result
    print("\n--- ⚖️ CLASSIFICATION ---")
    if output > 0.5:
        print("✅ RESULT: Digit identified as '1'. Neuron Fired!")
    else:
        print("❌ RESULT: Digit identified as '0'. Neuron stayed silent.")

    # 6. Evaluation
    if output > 0.5 and weight > 0:
        print("\n🏆 ARCHITECT: You successfully tuned the neuron to detect the signal!")
    else:
        print("\n⚠️ SIGNAL LOST: The signal was too weak or the bias was too high.")

if __name__ == "__main__":
    neural_network_game()
