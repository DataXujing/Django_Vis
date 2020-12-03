import pyecharts.options as opts
from pyecharts.charts import Line


def get_line(x_list,y_dict,project):

    line = Line().add_xaxis(xaxis_data=x_list)
    for y_val in y_dict.keys():
        line.add_yaxis(series_name=y_val,
                        y_axis=y_dict[y_val],
                        is_smooth=True,
                        markpoint_opts=opts.MarkPointOpts(
                        data=[
                            opts.MarkPointItem(type_="max", name="最大值"),
                            opts.MarkPointItem(type_="min", name="最小值"),
                            ]
                        ),
                         markline_opts=opts.MarkLineOpts(
                         data=[opts.MarkLineItem(type_="average", name="平均值")]
                        ),
                    )

    line.set_global_opts(
        title_opts=opts.TitleOpts(title="排行榜得分可视化", subtitle=project),
        # tooltip_opts=opts.TooltipOpts(trigger="axis"),
        toolbox_opts=opts.ToolboxOpts(is_show=True),
        # xaxis_opts=opts.AxisOpts( boundary_gap=False),

        xaxis_opts=opts.AxisOpts(
            axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
            is_scale=False,
            boundary_gap=False,
        )
    )
    line.set_series_opts(areastyle_opts=opts.AreaStyleOpts(opacity=0.5),)



    return line
    # render("temperature_change_line_chart.html")


if __name__ == "__main__":
    week_name_list = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    y = {"high_temperature":[11, 11, 15, 13, 12, 13, 10],
    "low_temperatur":[1, -2, 2, 5, 3, 2,0,1]}

    project = "哈哈"
    line = get_line(week_name_list,y,project)
    line.render("temperature_change_line_chart.html")

