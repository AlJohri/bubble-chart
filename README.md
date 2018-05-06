# exploratory data analysis

Let's do some exploratory data analysis with the house disbursements data to try and find a story.

First `cd` into the `house-expenditure` folder.

```
cd ~/Development/house-expenditure
```

Let's use an alias for `csvsql` to make typing queries a bit easier.

```
alias cs="csvsql -v --table tbl --no-inference --no-constraints --query"
```

### distinct_offices

```
cs "SELECT DISTINCT BIOGUIDE_ID, OFFICE FROM tbl" 2017Q4-house-disburse-detail.csv
```

### amount_by_category

```
cs "SELECT CATEGORY, SUM(AMOUNT) AS AMOUNT FROM tbl GROUP BY CATEGORY ORDER BY AMOUNT DESC" 2017Q4-house-disburse-detail.csv
```

#### amount_by_category for a congress person

```
cs "SELECT CATEGORY, SUM(AMOUNT) AS AMOUNT FROM tbl WHERE BIOGUIDE_ID='R000570' GROUP BY CATEGORY ORDER BY AMOUNT DESC" 2017Q4-house-disburse-detail.csv
```

```
R000570,HON. PAUL D. RYAN
P000197,HON. NANCY PELOSI
M001165,HON. KEVIN MCCARTHY
H000874,HON. STENY H. HOYER
S001176,HON. STEVE SCALISE
K000386,HON. JOHN KATKO
M000087,HON. CAROLYN B. MALONEY
E000297,HON. ADRIANO ESPAILLAT
C000714,HON. JOHN CONYERS JR.
```



-------------------------------------

```
cs "SELECT OFFICE, SUM(AMOUNT) AS AMOUNT FROM tbl WHERE PURPOSE='WATER' GROUP BY OFFICE ORDER BY AMOUNT DESC" 2017Q4-house-disburse-detail.csv
```
