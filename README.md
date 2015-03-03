# adu_testing
Testing code for the anomaly detection unit used in UCL CS module COMP3096

## testGen.py
* Reads each **spec.*.txt** file from the **tests** directory
* Outputs a **test.n.txt** file into the **tests** directory for each **spec.n.txt** *(where n = 0..)*

### spec.*.txt
These files specify the type of tests to be generated, each line of these files is formatted as `alt(temp, amount, start, end)`.
It is a call to the `alt()` function in **testGen.py**, which is used to modify synthetic temperature data to be stored in the **test.*.txt** file.
#### e.g.:
`alt(0,0.1,5,15)` indicates that the value for temperature **0** should increase by **0.1** each minute from minute **5** to minute **15**

### test.*.txt
These files contain the synthetic temperature data generated from the **spec.*.txt** files. The number of data points is determined by `TEST_SIZE` in **testGen.py**.

## blackbox.py
* Reads each **test.*.txt** file from the **tests** directory
* Anomaly scores are calculated for each data point in each of these files by using the historic data in **temperatures.log**
* This historic data is divided into multiple subsets of `WINDOW_SIZE` length
* Each is used in turn to calculate the anomaly scores for each data point in the test files
* These scores are stored in **scores.x.n.txt** files *(where x = test number, n = historic data subset number)*

## avgCalc.py
This is the script used to calculate the average of each temperature of all complete data points in **temperatures.log**. This provides a starting point for the generation of the synthetic data in **testGen.py**.

## blackbox.js
This is the original anomaly detection unit (ADU) that is used in our live system. **blackbox.py** is a transposition of this.
