
function graficoBarraV(titulo,valor,chartID){
  var ctx = document.getElementById(chartID);
  var names = JSON.parse(titulo);
  var prices = JSON.parse(valor);


  var productsChart = new Chart(ctx, {
    type: 'bar',

    data: {
      labels: names,
      datasets: [{
        label: 'Gastos R$',
        data: prices,
        backgroundColor: "#006400",
        borderColor: "006400",
        borderWidth: 1
      }]
    },

    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero:true
          }
        }]
      },
      legend: {
        display: false
      }
    },
  });
}


function graficoBarraH(titulo,valor,chartID){
  var ctx = document.getElementById(chartID);
  var names = JSON.parse(titulo);
  var prices = JSON.parse(valor);

  color=[]
  for (i=0;i<names.length;i++){

    if (i%2 == 0){
      color.push("#4B0082")
    }
    else{
      color.push("#00FF00")
    }
  }
  var productsChart = new Chart(ctx, {
    type: 'horizontalBar',
    data: {
      labels: names,
      datasets: [{
        label: 'Gastos R$',
        data: prices,
        backgroundColor: "#006400",
        borderColor: "006400",
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero:true
          }
        }]
      },
      legend: {
        display: false
      }
    },
  });
}

function graficoBarraP(titulo,valor,chartID){
  var ctx = document.getElementById(chartID);
  var names = JSON.parse(titulo);
  var prices = JSON.parse(valor);
  color2=["#CCFFFF", "#66FF99", "#99FF99", "#66FFFF", "#FF99FF","#33FF33" ,"#33CCFF" ,"#FFCCFF" ,"#00CC00" ,"#3366FF" ,"#CC33CC","#009900" ,"#3333FF" ,"#993366","#006600", "#000099", "#663366","#003300" ,"#000066", "#330033"]
  color=["#CCFFFF", "#66FF99", "#99FF99", "#66FFFF", "#FF99FF","#33FF33" ,"#33CCFF" ,"#FFCCFF" ,"#00CC00" ,'#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075', '#808080', '#ffffff', '#000000']

  // for (i=0;i<names.length;i++){
  //   var hexadecimais = '0123456789ABCDEF';
  //   var cor = '#';
  //     // Pega um número aleatório no array acima
  //     for (var i = 0; i < 6; i++ ) {
  //     //E concatena à variável cor
  //     cor += hexadecimais[Math.floor(Math.random() * 16)];
  //     color.push(cor)
  //   }
  // }

  var productsChart = new Chart(ctx, {
    type: 'pie',
    data: {
      labels: names,
      datasets: [{
        label: 'Gastos R$',
        data: prices,
        backgroundColor: color,
        borderColor: "006400",
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero:true
          }
        }]
      },
      legend: {
        display: false
      }
    },
  });
}


function graficoBarra3(titulo,valor1,valor2,valor3,chartID){
  var ctx = document.getElementById(chartID);
  var names = JSON.parse(titulo);
  var valor1 = JSON.parse(valor1);
  var valor2 = JSON.parse(valor2);
  var valor3 = JSON.parse(valor3);

  color=[]
  for (i=0;i<names.length;i++){

    if (i%2 == 0){
      color.push("#4B0082")
    }
    else{
      color.push("#00FF00 ")
    }
  }


  var productsChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: names,
      datasets: [{
        label: 'Saúde em R$',
        data: valor1,
        backgroundColor: "006400",
        borderColor: "006400",
        borderWidth: 1
      },
      {
        label: 'Educação em R$',
        data: valor2,
        backgroundColor: "FFFF00",
        borderColor: "FFFF00",
        borderWidth: 1
      },
      {
        label: 'Admin em R$',
        data: valor3,
        backgroundColor: "00FF00",
        borderColor: "00FF00",
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero:true
          }
        }]
      }
    }
  });
}

function graficoBarraV_Moeda(titulo,valor,chartID){
  var ctx = document.getElementById(chartID);
  var names = JSON.parse(titulo);
  var prices = JSON.parse(valor);


  var productsChart = new Chart(ctx, {
    type: 'bar',

    data: {
      labels: names,
      datasets: [{
        label: 'Gastos R$',
        data: prices,
        backgroundColor: "#006400",
        borderColor: "006400",
        borderWidth: 1
      }]
    },

    options: {

      scales: {
        yAxes: [{
          ticks: {
            beginAtZero:true
          }
        }]
      },

      legend: {
        display: false
      },

      tooltips: {
        callbacks: {
          label: function(tooltipItem, data) {
            var datasetLabel = data.datasets[tooltipItem.datasetIndex].label || 'Other';
            var value = data.datasets[0].data[tooltipItem.index];
            var label = data.labels[tooltipItem.index];
            return converteFloatMoeda(value);
          }
        }
      }
    },
  });
}

function converteFloatMoeda(valor){
  var inteiro = null, decimal = null, c = null, j = null;
  var aux = new Array();
  valor = ""+valor;
  c = valor.indexOf(".",0);
      //encontrou o ponto na string
      if(c > 0){
         //separa as partes em inteiro e decimal
         inteiro = valor.substring(0,c);
         decimal = valor.substring(c+1,valor.length);
       }else{
         inteiro = valor;
       }

      //pega a parte inteiro de 3 em 3 partes
      for (j = inteiro.length, c = 0; j > 0; j-=3, c++){
       aux[c]=inteiro.substring(j-3,j);
     }

      //percorre a string acrescentando os pontos
      inteiro = "";
      for(c = aux.length-1; c >= 0; c--){
       inteiro += aux[c]+'.';
     }
      //retirando o ultimo ponto e finalizando a parte inteiro
      
      inteiro = inteiro.substring(0,inteiro.length-1);
      
      decimal = parseInt(decimal);
      if(isNaN(decimal)){
       decimal = "00";
     }else{
       decimal = ""+decimal;
       if(decimal.length === 1){
        decimal = decimal+"0";
      }
    }


    valor = "R$ "+inteiro+","+decimal;


    return valor;
}