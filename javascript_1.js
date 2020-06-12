function infected(s) {
    let end_list = [];
    let total = 0;
    let infected = 0;
    let percentage = 0;

    let continent_list = s.split('X');
    for (let i=0; i < continent_list.length; i++) {
        let sick = continent_list[i].includes('1');
        if (sick) {
            end_list.push('1'.repeat(continent_list[i].length));
            infected += continent_list[i].length;
        } else {
            end_list.push(continent_list[i]);
        }
        total += continent_list[i].length;
    }
    
    if (total){
        percentage = infected/total*100;
    } else {
        percentage = 0;
    }
    let end = end_list.join('X');
    console.log(end_list)
    console.log(end);
    console.log(total);
    console.log(infected);
    console.log(percentage);

    return percentage;

  }

//   x = infected('01000000X000X011X0X')



