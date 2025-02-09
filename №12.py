silver_watch = 96
gold_watch = silver_watch / 16
total_revenue = int(input())
cost_silver_watch = 48
all_silver_watch = cost_silver_watch * silver_watch
cost_gold_watch = (total_revenue - all_silver_watch) / gold_watch
print(cost_gold_watch)
