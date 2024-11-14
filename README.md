# Agricultural Advisory System (AgriMitra)

**AgriMitra** is an advanced platform designed to revolutionize farming through machine learning, real-time analytics, and cloud computing. The system empowers farmers with insights into soil health, climate conditions, and market trends to enhance decision-making and productivity.

## Key Features

1. **Crop Recommendation**:
   - Provides crop suggestions based on environmental and soil conditions using Random Forest Regression.

2. **Crop Disease Identification**:
   - Utilizes VGG19 for image-based disease detection, enabling early intervention and reducing crop loss.

3. **MitraAI - Chatbot**:
   - An AI-driven conversational assistant offering 24/7 support for queries related to crop management, fertilizers, and pest control.

4. **Market Price Recommendations**:
   - Real-time updates on crop prices, helping farmers decide the optimal time for selling their produce.

## System Architecture

- **Frontend**: 
  - Built with Next.js and TypeScript for responsive and user-friendly interfaces.

- **Backend**:
  - Flask for handling API requests and coordinating with machine learning models.

- **Machine Learning Models**:
  - Random Forest for crop recommendation.
  - VGG19 for disease detection.
  - Gemini Pro 1.5 for the chatbot.

## Functionalities

- **Crop Recommendation**:
  - Input: Soil and weather data.
  - Output: Top 3 recommended crops based on user input.

- **Disease Detection**:
  - Input: Images of crops.
  - Output: Identified disease with recommended treatment.

- **Chatbot**:
  - Input: User queries in natural language.
  - Output: Personalized agricultural advice.

## System Requirements

### Hardware
- 64-bit Operating System
- 8 GB RAM (minimum)
- NVIDIA GTX 1060 or better GPU
- Network Speed: 200 Mbps and above

### Software
- Python 3.8+
- Flask, Next.js, TypeScript
- TensorFlow, Keras, PyTorch
- GitHub for version control

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/username/agrimitra.git

