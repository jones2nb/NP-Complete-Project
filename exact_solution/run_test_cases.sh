# This is the test case driver for the exact code
echo 
echo Running simple complete graph of size 3 input is test_in1.txt
time python3 exact_solution.py < test_in1.txt
echo ==================================================================
echo 
echo Running test complete graph size 10 input is medium_test.txt
time python3 exact_solution.py < medium_test.txt
echo ==================================================================
echo
echo Running test complete graph size 20 input is graph_size_20.txt
time python3 exact_solution.py < graph_size_20.txt
echo ==================================================================
echo
echo Running test random large graph input is Large Input
time python3 exact_solution.py < ../Large /Input
echo ==================================================================
echo
echo THE FOLLOWING TEST WILL TAKE A LONG TIME TO RUN
echo
echo Running test complete graph size 25 input is graph_size_25.txt
time python3 exact_solution.py < graph_size_25.txt
echo ==================================================================
echo
echo Running test complete graph size 30 input is graph_size_30.txt
time python3 exact_solution.py < graph_size_30.txt
echo ==================================================================
echo

