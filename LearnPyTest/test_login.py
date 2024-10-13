import pytest


# To check the version pytest --version
# function starts with test
# or function ends with test


# To run the test cases with same name in different files
# for example - test_login()  --  which is there in all files[test_demo, test_demo2].
# pytest -k login -v


# marker's
# @pytest.mark.markername
# to run the same -- pytest -m markername -vs
# to run with the filename -- pytest packagename/filename -m markername -vs


# to run the test cases parallelly
# pip install pytest-xdist
# pytest packagename/filename -n 3
# above 3 represents the number of browser to be opened


# to generate reports
# pip install pytest-html
# pytest packagename/filename -vs --html=filename.html


















































