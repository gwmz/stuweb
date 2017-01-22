// JavaScript Document
        // 基于准备好的dom，初始化echarts实例
var myChart = echarts.init(document.getElementById('plate_grade'));

// 指定图表的配置项和数据
var option = {
    tooltip: {
        trigger: 'item',
        formatter: "{a} <br/>{b}: {c} ({d}%)"
    },
    title: {
            text: '分数统计饼形图',
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
        data:['工数','代几','概率论','C语言','C++']
    },
    series: [
        {
	
	name:'分数',
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
	    {value:335, name:'工数'},
	    {value:310, name:'代几'},
	    {value:234, name:'概率论'},
	    {value:135, name:'C语言'},
	    {value:154, name:'C++'}
	]
        }
    ]
};
        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);