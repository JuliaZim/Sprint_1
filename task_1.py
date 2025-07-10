time_str = "1h 45m,360s,25m,30m 120s,2h 60s"
time_str = time_str.replace(" ", ",")
time_lst = time_str.split(",")

for i in range(len(time_lst)):
    if "h" in time_lst[i]:
        time_lst[i] = time_lst[i].replace("h", "")
        time_lst[i] = int(time_lst[i]) * 60
    elif "m" in time_lst[i]:
        time_lst[i] = int(time_lst[i].replace("m", ""))
    elif "s" in time_lst[i]:
        time_lst[i] = time_lst[i].replace("s", "")
        time_lst[i] = int(time_lst[i]) // 60

sum_time = sum(time_lst)
print(f"Общее количество минут: {sum_time}")
