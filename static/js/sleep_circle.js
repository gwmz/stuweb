// JavaScript Document
        // 基于准备好的dom，初始化echarts实例
var myChart = echarts.init(document.getElementById('plate_sleep'));

        // 指定图表的配置项和数据
var option = {
    tooltip: {
        trigger: 'item',
        formatter: "{a} <br/>{b}: {c} ({d}%)"
    },
    title: {
            text: '归宿情况统计图',
	    show: true,
	    x:'center',
	    style: {
		fontSize: 14,
		fontWeight: 'bolder',
		color: '#999'
	    }
    },
    legend: {
        orient: 'vertical',
        x: 'left',
        data:['非归宿天数','归宿天数']
    },
    series: [
        {
            name:'归宿情况',
            type:'pie',
            radius: ['40%', '60%'],
            avoidLabelOverlap: false,
            label: {
                normal: {
                    show: false,
                    position: 'center'
                },
                emphasis: {
                    show: true,
                    textStyle: {
                        fontSize: '30',
                        fontWeight: 'bold'
                    }
                }
            },
            labelLine: {
                normal: {
                    show: false
                }
            },
            data:[
                {value:335, name:'非归宿天数'},
                {value:310, name:'归宿天数'},
                
            ]
        }
    ]
};
// 使用刚指定的配置项和数据显示图表。
myChart.setOption(option);
