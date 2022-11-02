/*'create table cur_date(id int primary key, dt datetime default current_timestamp);'*/

/*
SELECT "Storage Bin", COUNT ("Storage Bin") as count_bin
FROM postings
WHERE "Reason Description" = "Cycle Counting"
GROUP BY "Storage Bin", "Reason Description"
Order by count_bin DESC
LIMIT 50;

*/

/*

SELECT COUNT(Result) FROM (SELECT "1","2","3","4","5","6","7","8","9","10",
        "11","12","13","14","15","16","17","18","19","20","21","22",
        "23","24","25","26","27","28","29","30","31","32","33","34",
        "35","36","37","38","39","40","41","42","43","44","45","46",
        "47","48","49","50","51","52",
        "1"+"2"+"3"+"4"+"5"+"6"+"7"+"8"+"9"+"10"+"11"+"12"+"13"+"14"
        +"15"+"16"+"17"+"18"+"19"+"20"+"21"+"22"+"23"+"24"+"25"+"26"+
        "27"+"28"+"29"+"30"+"31"+"32"+"33"+"34"+"35"+"36"+"37"+"38"+"39"
        +"40"+"41"+"42"+"43"+"44"+"45"+"46"+"47"+"48"+"49"+"50"+"51"+"52" 
        AS Result FROM MKI) WHERE Result > 0;
*/		

/*
SELECT (SELECT COUNT(*) FROM countings) - (SELECT COUNT(*) FROM countings WHERE Counted > 0) AS Differance;
*/

/*
SELECT "Physical Inventory Document", 
COUNT(*) as counted
FROM postings
WHERE "Reason Description" = "Cycle Counting"
GROUP BY "Physical Inventory Document"
ORDER BY counted DESC
LIMIT (10)
*/

/*
UPDATE MKI SET 
"1" = 0,
"2" = 0,
"3" = 0,
"4" = 0,
"5" = 0,
"6" = 0,
"7" = 0,
"8" = 0,
"9" = 0,
"10" = 0,
"11" = 0,
"12" = 0,
"13" = 0,
"14" = 0,
"15" = 0,
"16" = 0,
"17" = 0,
"18" = 0,
"19" = 0,
"20" = 0,
"21" = 0,
"22" = 0,
"23" = 0,
"24" = 0,
"25" = 0,
"26" = 0,
"27" = 0,
"28" = 0,
"29" = 0,
"30" = 0,
"31" = 0,
"32" = 0,
"33" = 0,
"34" = 0,
"35" = 0,
"36" = 0,
"37" = 0,
"38" = 0,
"39" = 0,
"40" = 0,
"41" = 0,
"42" = 0,
"43" = 0,
"44" = 0,
"45" = 0,
"46" = 0,
"47" = 0,
"48" = 0,
"49" = 0,
"50" = 0,
"51" = 0,
"52" = 0;
*/

--JTS1

/*
UPDATE JTS1 SET 
"1" = 0,
"2" = 0,
"3" = 0,
"4" = 0,
"5" = 0,
"6" = 0,
"7" = 0,
"8" = 0,
"9" = 0,
"10" = 0,
"11" = 0,
"12" = 0,
"13" = 0,
"14" = 0,
"15" = 0,
"16" = 0,
"17" = 0,
"18" = 0,
"19" = 0,
"20" = 0,
"21" = 0,
"22" = 0,
"23" = 0,
"24" = 0,
"25" = 0,
"26" = 0,
"27" = 0,
"28" = 0,
"29" = 0,
"30" = 0,
"31" = 0,
"32" = 0,
"33" = 0,
"34" = 0,
"35" = 0,
"36" = 0,
"37" = 0,
"38" = 0,
"39" = 0,
"40" = 0,
"41" = 0,
"42" = 0,
"43" = 0,
"44" = 0,
"45" = 0,
"46" = 0,
"47" = 0,
"48" = 0,
"49" = 0,
"50" = 0,
"51" = 0,
"52" = 0;
*/

--JTS2

/*
UPDATE JTS2 SET 
"1" = 0,
"2" = 0,
"3" = 0,
"4" = 0,
"5" = 0,
"6" = 0,
"7" = 0,
"8" = 0,
"9" = 0,
"10" = 0,
"11" = 0,
"12" = 0,
"13" = 0,
"14" = 0,
"15" = 0,
"16" = 0,
"17" = 0,
"18" = 0,
"19" = 0,
"20" = 0,
"21" = 0,
"22" = 0,
"23" = 0,
"24" = 0,
"25" = 0,
"26" = 0,
"27" = 0,
"28" = 0,
"29" = 0,
"30" = 0,
"31" = 0,
"32" = 0,
"33" = 0,
"34" = 0,
"35" = 0,
"36" = 0,
"37" = 0,
"38" = 0,
"39" = 0,
"40" = 0,
"41" = 0,
"42" = 0,
"43" = 0,
"44" = 0,
"45" = 0,
"46" = 0,
"47" = 0,
"48" = 0,
"49" = 0,
"50" = 0,
"51" = 0,
"52" = 0;
*/

-- query = f'''
-- INSERT INTO postings
-- ("Higher-Level Handling Unit", "Physical Inventory Document", "Item","Document Year",\
-- "Physical Inventory Procedure","Physical Inventory Status", "Activity Area","Reason","Reason Description","Priority",\
-- "Priority Description",	"Created On","Created At","Count Date","Count Time","Counter","Posting Date","Changed By","Time of Posting",	\
-- "Inventory Blocking Ind.","Storage Bin Empty","Storage Type","Storage Section","Storage Bin","Product","Product Short Description",	\
-- "Batch","Stock Type","Warehouse Order","Warehouse Task","Book Quantity","Counted Quantity","Difference Quantity","Absolute Difference", \
-- "Quantity","Base Unit of Measure","Difference Value","Absolute Difference Value","Currency","Difference Qty to Target Qty in Percent.")\
--  VALUES({})'''