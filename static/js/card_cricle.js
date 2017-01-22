
var myChart = echarts.init(document.getElementById('plate_card'));

// 指定图表的配置项和数据
var option = {
    tooltip: {
        trigger: 'item',
        formatter: "{a} <br/>{b}: {c} ({d}%)"
    },
    title: {
        text: '一卡通情况',
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
        data:['正常','异常']
    },
    series: [
        {
            name:'天数',
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
                {value:335, name:'正常'},
                {value:310, name:'异常'},
                
            ]
        }
    ]
};
        // 使用刚指定的配置项和数据显示图表。
myChart.setOption(option);