#include<graphics.h>
#include<time.h>
#include<math.h>
#include<dos.h>
#include<stdio.h>
#define PI 3.14569
void sounder();
void bibin();
void main()
{
int gd=DETECT,gm;
time_t start, finish, now;
     struct tm *ptr;
     char *c, buf1[80],h[3],m[3],s[3];
     double duration;
     int i=0,j,k,x,y,xm,ym,xh,yh;


     /* Record the time the program starts execution. */

initgraph(&gd,&gm,"e:\tc\bgi");
clrscr();
setfillstyle(SOLID_FILL,BLUE);

bar3d(170,100,470,400,10,1);


setcolor(GREEN);
circle(320,250,100);//for outercircle inner radius
circle(320,250,125);//for outercircle outer radius
circle(320,250,1);//for innercircle inner radius
circle(320,250,7);//for innercircle outer radius
setfillstyle(SOLID_FILL,RED); //for outercircle filling red color
floodfill(430,250,GREEN);//filling outercircle with green border
floodfill(320,250,GREEN);
setfillstyle(SOLID_FILL,MAGENTA); //for innercircle filling mangenta
floodfill(325,250,GREEN); //filling innercilling with green border
settextstyle(1,0,1);
setcolor(15);
outtextxy(318,352,"6");
outtextxy(376,334,"5");
outtextxy(410,294,"4");
outtextxy(430,237,"3");
outtextxy(417,186,"2");
outtextxy(376,144,"1");
outtextxy(310,127,"12");
outtextxy(254,140,"11");
outtextxy(213,182,"10");
outtextxy(206,237,"9");
outtextxy(221,301,"8");
outtextxy(261,338,"7");
/* Record the current time, using the alternate method of */
     /* calling time(). */

    time(&now);

     /* Convert the time_t value into a type tm structure. */

     ptr = localtime(&now);

     /* Create and display a formatted string containing */
     /* the current time. */

    c = asctime(ptr);
    h[0]=c[11];
    h[1]=c[12];
    m[0]=c[14];
    m[1]=c[15];
    s[0]=c[17];
    s[1]=c[18];
    i=atoi(h);
    if(i>11) i=i-12;
    j=atoi(m);
    xm=320+80*(sin(PI/30*j));
                ym=250-80*(cos(PI/30*j));
                xh=320+60*sin(PI/6*i+PI/360*j);
                yh=250-60*cos(PI/6*i+PI/360*j);
                 setlinestyle(SOLID_LINE,1,3);
                 setcolor(BROWN);
                 line(320,250,xm,ym);
                  setcolor(MAGENTA);
                  line(320,250,xh,yh);
                 setbkcolor(GREEN);
sounder();

getch();
bibin();
closegraph();
restorecrtmode();
}

void sounder()
{
int frequency;
for(frequency=4000;frequency<5000;frequency++)
sound(frequency);
nosound();
return;
}
void bibin()
{
int midx=320,midy=230;

     cleardevice();
    
    delay(4000);
    return ;
}
