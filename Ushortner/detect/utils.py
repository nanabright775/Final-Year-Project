# # detect/utils.py
# import joblib
# import tldextract

# # Load the pre-trained model
# model = joblib.load('path/to/url_detector_model.pkl')

# def extract_features(url):
#     ext = tldextract.extract(url)
#     return f"{ext.domain}.{ext.suffix}"

# def is_malicious(url):
#     features = extract_features(url)
#     return model.predict([features])[0] == 1
