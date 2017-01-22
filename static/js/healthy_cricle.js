
var myChart = echarts.init(document.getElementById('plate_healthy'));

// 指定图表的配置项和数据
var option = {
    tooltip: {
        trigger: 'item',
        formatter: "{a} <br/>{b}: {c} ({d}%)"
    },
    title: {
        text: '健康情况',
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
        data:['健康','非健康']
    },
    series: [
        {
            name:'人数',
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
                {value:335, name:'健康'},
                {value:310, name:'非健康'}
            ]
        }
    ]
};
        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
