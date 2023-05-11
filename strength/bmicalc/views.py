from django.shortcuts import render

def MainView(request):
        context = {}
        if request.method == "POST":
                weight = float(request.POST.get("weight-metric"))
                height = float(request.POST.get("height-metric"))

                bmi = ((weight)/(height**2))

                if bmi < 16:
                        state = "Severe Thinness"
                elif bmi > 16 and bmi < 17:
                        state = "Moderate Thinness"
                elif bmi > 17 and bmi < 18.5:
                        state = "Mild Thinness"
                elif bmi > 18.5 and bmi < 25:
                        state = "Normal"
                elif bmi > 25 and bmi <30:
                        state = "Overweight"
                elif bmi > 30 and bmi <35:
                        state = "Overweight type I"
                elif bmi > 35 and bmi <40:
                        state = "Overweight type II"
                elif bmi > 40:
                        state = "Overweight type III"

                context["bmi"] = round(bmi, 2)
                context["state"] = state 
                        
        return render(request, "bmicalc/main.html", context)
                        
                        