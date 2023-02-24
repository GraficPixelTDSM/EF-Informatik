![](./images/Intro.png)
```

module bausteinT() {
    union() {
        cube([3, 1, 1]);
        translate([1, 0, 1])
            cube([1, 1, 1]);
    }
}
module bausteinL(){
    translate([4, 0, 0]) union(){
        translate([0, 0, 1]) cube([1, 1, 1]);
        cube([3, 1, 1]);
    }
}
module bausteinEck3(){
    translate([0, 2, 0]) union(){
        translate([0, 0, 1]) cube([1, 1, 1]);
        cube([2, 1, 1]);
        translate([0, 1, 0]) cube([1, 1, 1]);
    }
}
module bausteinEck23(){
    translate([3, 2, 0]) union(){
        translate([0, 0, 1]) cube([1, 1, 1]);
        cube([2, 1, 1]);
        translate([0, 1, 0]) cube([1, 1, 1]);
    }
}
module bausteinS(){
    translate([1, 5, 0]) union(){
        cube([2, 1, 1]);
        translate([-1, 1, 0]) cube([2, 1, 1]);
    }
}
module bausteinEck(){
    translate([6, 2, 0]) union(){
        cube([1, 2, 1]);
        translate([1, 0, 0]) cube([1, 1, 1]);
    }
}
module bausteinSch(){
    translate([4, 5, 0]) union(){
        cube([1, 2, 1]);
        translate([1, 0, 0]) cube([1, 1, 2]);
    }
}

rotate([0, 0, 0])
    scale([1, 1, 1])
        bausteinT();
        bausteinEck3();
        bausteinEck23();
        bausteinEck();
        bausteinL();
        bausteinS();
        bausteinSch();
```