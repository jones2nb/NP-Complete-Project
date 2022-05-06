# This is the test case driver for the exact code
echo 
echo Running simple complete graph of size 3 input is test_1.txt
time python3 cs412_exact.py < test_cases/test_1.txt
echo ==================================================================
echo 
echo Running test complete graph size 10 input is test_2.txt
time python3 cs412_exact.py < test_cases/test_2.txt
echo ==================================================================
echo
echo Running test complete graph size 20 input is test_3.txt
time python3 cs412_exact.py < test_cases/test_3.txt
echo ==================================================================
echo
echo Running test random large graph input is test_4.txt
time python3 cs412_exact.py < test_cases/test_4.txt
echo ==================================================================
echo
echo THE FOLLOWING TEST WILL TAKE A LONG TIME TO RUN
echo
echo Running test complete graph size 25 input is test_5.txt
time python3 cs412_exact.py < test_cases/test_5.txt
echo ==================================================================
echo
echo Running test complete graph size 30 input is test_6.txt
time python3 cs412_exact.py < test_cases/test_6.txt
echo ==================================================================
echo

