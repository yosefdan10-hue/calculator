[1mdiff --git a/stats.py b/stats.py[m
[1mindex 56d83b0..6fa2bf0 100644[m
[1m--- a/stats.py[m
[1m+++ b/stats.py[m
[36m@@ -30,6 +30,7 @@[m [mdef median(numbers):[m
         return None[m
 [m
     numbers = sorted(numbers)[m
[32m+[m
     n = len(numbers)[m
     mid = n // 2[m
 [m
