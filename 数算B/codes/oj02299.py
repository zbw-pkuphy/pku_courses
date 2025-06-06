name_num=dict()
namel=[]
ansl=[]
n=int(input())
for i in range(n):
    s=input().strip()
    j=s.rfind("-")
    name=s[:j]
    num=float(s[j+1:-1]) if s[-1]=="M" else float(s[j+1:-1])*1000
    if name in namel:
        name_num[name].append([s[j+1:],num])
    else:
        name_num[name]=[[s[j+1:],num]]
        namel.append(name)
namel.sort()
for name in namel:
    name_num[name].sort(key=lambda x:x[1])
    print(f"{name}: {', '.join([i[0] for i in name_num[name]])}")

# n = int(input())
# model_dict = {}
# for _ in range(n):
#     line = input().strip()
#     last_dash = line.rfind('-')
#     model_name = line[:last_dash]
#     param_str = line[last_dash+1:]
    
#     # 处理参数字符串
#     unit = param_str[-1]
#     num_str = param_str[:-1]
#     num = float(num_str)
#     converted = num * 1000 if unit == 'B' else num
    
#     # 更新字典
#     if model_name not in model_dict:
#         model_dict[model_name] = []
#     model_dict[model_name].append((param_str, converted))

# # 对模型名称进行排序
# sorted_models = sorted(model_dict.keys())

# for model in sorted_models:
#     # 对参数列表按转换后的值排序
#     sorted_params = sorted(model_dict[model], key=lambda x: x[1])
#     param_list = [param[0] for param in sorted_params]
#     print(f"{model}: {', '.join(param_list)}")