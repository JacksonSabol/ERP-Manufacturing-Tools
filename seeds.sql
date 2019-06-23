USE erp_manufacturing_tools;

INSERT INTO sales (department_name, amount)
VALUES
  ("Minor Hardware", 1234.56),
  ("LIDAR", 4321.00),
  ("Cabling", 333.33);

SELECT * FROM sales