from pydantic import BaseModel, Field
from enum import Enum
from typing import List, Dict

class IntensityLevel(str, Enum):
    LOW = "Low"
    MODERATE = "Moderate"
    HIGH = "High"
    EXTREME = "Extreme"

class HealthPlan(BaseModel):
    # Nutrition
    dietary_guidelines: str = Field(..., description="General dietary advice")
    meal_plan_schedule: List[Dict[str, str]] = Field(..., description="Meal plan list")
    supplement_list: List[str] = Field(..., description="List of supplements")

    # Sleep
    optimal_sleep_duration: str = Field(..., description="Recommended sleep range")
    sleep_improvement_tips: List[str] = Field(..., description="List of sleep tips")

    # Workout
    daily_workout_split: Dict[str, str] = Field(..., description="Workout plan per day")
    weekly_workout_schedule: Dict[str, str] = Field(..., description="Weekly schedule")

    # Intensity
    workout_intensity_level: IntensityLevel = Field(..., description="Overall intensity level")
    target_heart_rate_zone: str = Field(..., description="Ideal heart rate during workout")
    perceived_exertion_scale: str = Field(..., description="RPE scale from 1-10")

    # Calorie Data
    total_daily_energy_expenditure: int = Field(..., description="TDEE in calories")
    calorie_adjustment: int = Field(..., description="Surplus or deficit for goals")
    macro_distribution_ratios: Dict[str, float] = Field(..., description="Macro ratios")

    # Motivation
    daily_motivational_quote: str = Field(..., description="Motivational quote")
    expected_progress_timeline: str = Field(..., description="Expected visible results")
