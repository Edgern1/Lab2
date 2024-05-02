import Lab2
def test_minmax():
	assert [1,100]==Lab2.calc_min_max_temperature([1,2,34,100])
def test_avg():
	assert 34.25==Lab2.calc_average_temperature([1,2,34,100])
def test_median():
	assert 18==Lab2.calc_median_temperature([1,2,34,100])
