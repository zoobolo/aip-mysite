class ExerciseSession:
    
    def __init__ (self, exercise, intensity, duration):
        self.exercise = exercise
        self.intensity = intensity
        self.duration = duration
       
    def set_exercise (self,newExercise):
        self.exercise = newExercise
    
    def set_intensity (self, newIntensity):
        self.intensity = newIntensity
    
    def set_duration (self, newDuration):
        self.duration = newDuration
        
    def calories_burned (self):
    
        if self.intensity == "Low":
            calories_burned = ( 4 * self.duration)
        elif self.intensity == "Moderate":
            calories_burned = (8 * self.duration)
        else:
            calories_burned = (12 * self.duration)       
        return calories_burned


new_exercise = ExerciseSession("Running", "Low", 60)
print(new_exercise.calories_burned())
new_exercise.set_exercise("Swimming")
new_exercise.set_intensity("High")
new_exercise.set_duration(30)
print(new_exercise.calories_burned())

