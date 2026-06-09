**TASK 4: OPTIMIZATION MODEL**

Production Optimization using Linear Programming

**OBJECTIVE**

This project focuses on solving a business optimization problem using Linear Programming. The goal is to determine the optimal production quantities of two products while satisfying resource constraints and maximizing profit.

**PROBLEM STATEMENT**

A company manufactures two products:

* Product A earns ₹50 profit per unit.
* Product B earns ₹40 profit per unit.

Resource Constraints:

* 2A + B ≤ 100
* A + B ≤ 80

The objective is to maximize total profit while adhering to these constraints.

**TECHNOLOGIES USED**

* Python
* NumPy
* SciPy
* Matplotlib

**OPTIMIZATION METHOD**

Linear Programming was implemented using SciPy's `linprog()` function.

The optimization model:

Maximize:

Profit = 50A + 40B

Subject to:

* 2A + B ≤ 100
* A + B ≤ 80
* A ≥ 0
* B ≥ 0

**IMPLEMENTATION STEPS**

**1. Problem Definition**

* Defined the profit function.
* Specified resource constraints.

**2. Model Formulation**

* Converted the maximization problem into a minimization problem for SciPy.
* Defined decision variables and bounds.

**3. Optimization**

* Applied Linear Programming using `linprog()`.
* Calculated optimal production quantities.

**4. Visualization**

* Generated a graph showing optimal production quantities.
* Saved the graph as an image file.

**RESULTS**

Optimal Production:

* Product A = 20 Units
* Product B = 60 Units

Maximum Profit:

* ₹3400

**OUTPUT FILES**

* optimization_model.py
* optimization_graph.png

**HOW TO RUN**

Install Dependencies:

pip install numpy scipy matplotlib

Run Program:

python optimization_model.py

**OUTPUT**

* Optimal production quantities
* Maximum profit calculation
* Production optimization graph

**KEY LEARNING**

* Linear Programming concepts
* Optimization techniques
* Business decision-making using mathematics
* Using SciPy for optimization problems
* Data visualization with Matplotlib

**CONCLUSION**

This project demonstrates how Linear Programming can be used to solve real-world business optimization problems. By determining optimal production quantities, organizations can maximize profit while efficiently utilizing available resources.

**AUTHOR**

Bonthala Supriya Sindhu
