# Airbnb Price Prediction

## Objective
Predict Airbnb listing prices using listing features.

## Model Used
- Linear Regression 

## Results A >> Used room_type,neighbourhood and neighbouhood_group
- MAE: ~67
- R²: ~0.12

## Results B
- MAE: ~68
- R²: ~0.13

## Observations
- Room type and neighbourhood are the strongest features.
- Availability and minimum nights have weak correlation with price.
- Linear regression performs poorly due to non-linear relationships in the data.
- Adding more features increases the r score but only by a little margin

## Conclusion
The linear model provides a baseline but is not sufficient for accurate predictions. Future work will explore non-linear models such as Random Forest or Gradient Boosting.