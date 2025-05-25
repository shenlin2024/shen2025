from pyecharts.charts import Bar
from pyecharts import options as opts
from dbUtil import db
def generate_job_chart(db):
    # 执行 SQL 查询
    cursor = db.cursor()
    sql = """
        SELECT 
            job_city, 
            COUNT(*) AS job_count 
        FROM s_job  -- 请替换为你的实际表名
        GROUP BY job_city 
        ORDER BY job_count DESC
    """
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()

    # 处理查询结果
    cities = [row[0] for row in results]
    counts = [row[1] for row in results]

    # 创建柱状图
    bar = (
        Bar(init_opts=opts.InitOpts(theme="light", width="1000px", height="600px"))
        .add_xaxis(cities)
        .add_yaxis("岗位数量", counts)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="各城市工作岗位数量统计"),
            xaxis_opts=opts.AxisOpts(
                name="城市",
                axislabel_opts={"rotate": 45},  # 城市名称倾斜 45 度
            ),
            yaxis_opts=opts.AxisOpts(name="数量"),
            datazoom_opts=[opts.DataZoomOpts()],  # 添加数据缩放
        )
        .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值")
                ]
            )
        )
    )

    # 生成 HTML 文件
    bar.render("job_statistics.html")
    print("图表已生成到 job_statistics.html")

# 使用示例
if __name__ == "__main__":
    generate_job_chart(db)
    db.close()  # 关闭连接
