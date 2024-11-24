import streamlit as st

import math as mf

# basic formatting 

st.title("Measurement and Geometry")
st.code("Exploring Surface Area and Volume; by Armaan.")

# begin calculator 1, 3d surface area & volume for prisms & pyramids

option = st.selectbox("Enter the name of the shape you'd like to analyse.", ["Cylinder", "Sphere", "Prism", "Pyramid"])
if option == "Cylinder":
    rord = st.selectbox("Would you like to input diameter or radius?", ["Diameter", "Radius"])
    st.write("Given")
    if rord == "Diameter":
            st.latex(r'''
            V = \pi \left(\frac{d}{2}\right)^2 h 
            ''')
            cd = int(st.number_input("Please enter the diameter of your cylinder's base."))
            ch = int(st.number_input("Please enter the height of your cylinder"))
            diamradiusconst = 2
            cdintor = cd / diamradiusconst
            pi = 3.1415
            r2 = cdintor ** 2
            vcylindre = pi * r2 * ch
            unitscubed = u'³'
            unitscubedfull = f''' units {unitscubed} '''
            st.write(f''' The volume of your cylinder is {vcylindre} {unitscubedfull}''')
            st.write("And given")
            st.latex(r'''
            SA = 2 \pi r h + 2 \pi r^2       
            ''')
            sacylinder = 2 * pi * cdintor * (cdintor + ch)
            unitssquared = u'²'
            unitssquaredfull = f''' units {unitssquared} '''
            st.write(f''' The surface area of your cylinder is {sacylinder} {unitssquaredfull}''')
    else:
          if rord == "Radius":
                st.latex(r'''
                V = \pi r^2 h     
                ''')
                cr = int(st.number_input("Please enter the radius of your cylindre's base."))
                ch = int(st.number_input("Please enter your cylindre's height."))
                pi = 3.1415
                realr2 = cr ** 2
                vcylindre = pi * realr2 * ch
                unitscubed = u'³'
                unitscubedfull = f''' units {unitscubed} '''
                st.write(f''' The volume of your cylindre is {vcylindre} {unitscubedfull}''')
                st.write("And given")
                st.latex(r'''
                SA = 2 \pi r h + 2 \pi r^2       
                ''')
                sacylinder = 2 * pi * cr * (cr + ch)
                unitssquared = u'²'
                unitssquaredfull = f''' units {unitssquared} '''
                st.write(f''' The surface area of your cylinder is {sacylinder} {unitssquaredfull}''')
elif option == "Sphere":
            rords = st.selectbox("Would you like to input diameter or radius?", ["Diameter", "Radius"])
            st.write("Given")
            if rords == "Diameter":
                  st.latex(r'''
                  V = \left(\frac{4}{3}\right) \pi \left(\frac{d}{2}\right)^3     
                  ''')
                  sd = int(st.number_input("Please enter the diameter of your sphere's base."))
                  rforsphere = sd / 2
                  fouroverthree = 4 / 3
                  rcubedsphere = rforsphere ** 3
                  pi = 3.1413
                  vsphere = fouroverthree * pi * rcubedsphere 
                  unitscubed = u'³'
                  unitscubedfull = f''' units {unitscubed} '''
                  st.write(f''' The volume of your sphere is {vsphere} {unitscubedfull}''')
                  st.write("And given")
                  st.latex(r'''
                  SA = 4 \pi r^2       
                  ''')
                  sasphere = 4 * pi * (rforsphere ** 2)
                  unitssquared = u'²'
                  unitssquaredfull = f''' units {unitssquared} '''
                  st.write(f''' The surface area of your sphere is {sasphere} {unitssquaredfull}''')
            else:
                  if rords == "Radius":
                        st.latex(r'''
                        V = \left(\frac{4}{3}\right) \pi r^3    
                        ''')
                        sr = (st.number_input("Please enter the radius of your sphere."))
                        pi = 3.1415
                        fouroverthree = 4/3
                        rcubedsphere = sr ** 3
                        vsphere = fouroverthree * pi * rcubedsphere
                        unitscubed = u'³'
                        unitscubedfull = f''' units {unitscubed} '''
                        st.write(f''' The volume of your sphere is {vsphere} {unitscubedfull}''')
                        st.write("And given")
                        st.latex(r'''
                        SA = 4 \pi r^2       
                        ''')
                        sasphere = 4 * pi * (sr ** 2)
                        unitssquared = u'²'
                        unitssquaredfull = f''' units {unitssquared} '''
                        st.write(f''' The surface area of your sphere is {sasphere} {unitssquaredfull}''')
elif option == "Prism":
       prismbaseshape = st.number_input("How many sides does the base of your shape have?", min_value=3, max_value=9)
       if prismbaseshape == 3:
              st.write("Given")
              st.latex(r'''
              V = \left(\frac{1}{2}\right) b h d       
              ''')
              triangularprismbase = st.number_input("Please enter the length of the base of your triangular prism.")
              triangularprismheight = st.number_input("Please enter the  height of this triangular base.")
              triangularprismrealheight = st.number_input("Please enter the height of your prism.")
              oneovertwo = 1 / 2
              volumeoftriangularp = oneovertwo * triangularprismbase * triangularprismheight * triangularprismrealheight
              unitscubed = u'³'
              unitscubedfull = f''' units {unitscubed} '''
              st.write(f''' The volume of your triangular prism is {volumeoftriangularp} {unitscubedfull}''')
              st.write("To determine surface area, please enter all 3 side lengths of your prism's base.")
              triangularsidelength1 = st.number_input("Side length 1:")
              triangularsidelength2 = st.number_input("Side length 2:")
              triangularsidelength3 = st.number_input("Side length 3:")
              st.write("Given")
              st.latex(r'''
              SA = B + LA       
              ''', help = " Where B = base area, LA = lateral area")
              triangularprismperimeter = triangularsidelength1 + triangularsidelength2 + triangularsidelength3
              triangularprismlateralarea = triangularprismperimeter * triangularprismrealheight
              triangularprismbasearea = triangularprismbase * triangularprismheight
              surfaceareatriangularprism = triangularprismbasearea + triangularprismlateralarea
              unitssquared = u'²'
              unitssquaredfull = f''' units {unitssquared} '''
              st.write(f''' The surface area of your triangular prism is {surfaceareatriangularprism} {unitssquaredfull}''')
       elif prismbaseshape == 4:
              st.write("Given")
              st.latex(r'''
              V = lwh       
              ''')
              regularprismbase = st.number_input("Please enter the length of the base of your prism.")
              regularprismheight = st.number_input("Please enter the width of the base of your prism.")
              regularprismrealheight = st.number_input("Please enter the height of your prism.")
              volumeofregularp = regularprismbase * regularprismheight * regularprismrealheight
              unitscubed = u'³'
              unitscubedfull = f''' units {unitscubed} '''
              st.write(f''' The volume of your triangular prism is {volumeofregularp} {unitscubedfull}''')
              st.write("Given")
              st.latex(r'''
              SA = B + LA       
              ''', help = " Where B = base area, LA = lateral area")
              regularprismsa = 2 * regularprismbase * regularprismheight + 2 * regularprismbase * regularprismrealheight + 2 * regularprismheight * regularprismrealheight
              unitssquared = u'²'
              unitssquaredfull = f''' units {unitssquared} '''
              st.write(f''' The surface area of your prism is {regularprismsa} {unitssquaredfull}''')
       elif prismbaseshape == 5:
              st.write("Given")
              st.latex(r'''
              V = \left(\frac{1}{2}\right) (e1 + e2)  h l         
              ''', help = "Where e1 and e2 are the two base lengths of the trapezoid base.") 
              trapezoidbaseedgeone = st.number_input("Please enter one of the side lengths of your trapezoid's base.")
              trapezoidbaseedgetwo = st.number_input("Please enter the other edge length of your trapezoid's base")
              trapezoidbaseheight = st.number_input("Please enter the height of your trapezoid prism's base.")
              trapezoidprismheight = st.number_input("Please enter the height of your prism")
              oneovertwo = 1 / 2
              trapezoidapethom = trapezoidbaseedgeone + trapezoidbaseedgetwo
              trapezoidv = oneovertwo * trapezoidapethom * trapezoidbaseheight * trapezoidprismheight
              unitscubed = u'³'
              unitscubedfull = f''' units {unitscubed} '''
              st.write(f''' The volume of your prism is {trapezoidv} {unitscubedfull}''')
              st.write("Given")
              st.latex(r'''
              SA = B + LA       
              ''', help = " Where B = base area, LA = lateral area")
              st.write("Please provide the two edge lengths of the base of the trapezoid.")
              trapeziodsidelength1 = st.number_input("Side length 1.")
              trapezoidsidelength2 = st.number_input("Side length 2.")
              trapezoidperimeter = trapeziodsidelength1 + trapezoidsidelength2 + trapezoidbaseedgeone + trapezoidbaseedgetwo
              trapezoidsurfacearea = (trapezoidbaseedgeone + trapezoidbaseedgetwo) * trapezoidbaseheight + (trapezoidperimeter * trapezoidprismheight)
              unitssquared = u'²'
              unitssquaredfull = f''' units {unitssquared} '''
              st.write(f''' The surface area of your prism is {trapezoidsurfacearea} {unitssquaredfull}''')
       elif prismbaseshape == 6:
              st.write("Given")
              st.latex(r'''
              V = \left(\frac{APh}{2}\right)     
              ''', help = "Where A = apothem, P = perimeter, and h = prism height.")
              slengthhex = st.number_input("Please enter a side length of your hexagonal base.")
              hexpheight = st.number_input("Pleae enter the height of your prism.")
              squarerootthree = mf.sqrt(3)
              productsqrthex = squarerootthree * 3
              quotientsqrthex = productsqrthex / 2
              slsquaredhex = slengthhex ** 2 
              vhexagon = quotientsqrthex * slsquaredhex * hexpheight
              unitscubed = u'³'
              unitscubedfull = f''' units {unitscubed} '''
              st.write(f''' The volume of your prism is {vhexagon} {unitscubedfull}''')
              st.write("Given")
              st.latex(r'''
              SA = B + LA       
              ''', help = " Where B = base area, LA = lateral area")
              surfaceareahexagon = 6 * slengthhex * hexpheight + 3 * mf.sqrt(3) * slengthhex ** 2
              unitssquared = u'²'
              unitssquaredfull = f''' units {unitssquared} '''
              st.write(f''' The surface area of your prism is {surfaceareahexagon} {unitssquaredfull}''')
       elif prismbaseshape == 7:
              st.write("Given")
              st.latex(r'''
              V = \left(\frac{APh}{2}\right)        
              ''', help = "Where A = apothem, P = perimeter, and h = prism height.")
              septogons = st.number_input("Please enter a side length for your heptogon.")
              septogonprismheight = st.number_input("Please enter the height of your prism.")
              vheptogon = ((7 * septogons ** 2 / 4) * (1 / (mf.tan(3.1415/7)))) * septogonprismheight
              unitscubed = u'³'
              unitscubedfull = f''' units {unitscubed} '''
              st.write(f''' The volume of your prism is {vheptogon} {unitscubedfull}''')
              st.write("Given")
              st.latex(r'''
              SA = B + LA       
              ''', help = " Where B = base area, LA = lateral area")
              surfaceareheptogon = (7 / 2) * (septogons ** 2) * 2.0765 + (7 * septogons * septogonprismheight)
              unitssquared = u'²'
              unitssquaredfull = f''' units {unitssquared} '''
              st.write(f''' The surface area of your prism is {surfaceareheptogon} {unitssquaredfull}''')
       elif prismbaseshape == 8:
              st.write("Given")
              st.latex(r'''
              V = \left(\frac{APh}{2}\right)        
              ''', help = "Where A = apothem, P = perimeter, and h = prism height.")
              octogons = st.number_input("Please enter a side length from your octogonal base.")
              octogonprismh = st.number_input("Please enter the height of your prism.")
              sqrtoctoapothem = 1 + mf.sqrt(2)
              voctogon = 2 * sqrtoctoapothem * octogons ** 2
              voctogonprism = voctogon * octogonprismh
              unitscubed = u'³'
              unitscubedfull = f''' units {unitscubed} '''
              st.write(f''' The volume of your octogonal prism is {voctogonprism} {unitscubedfull}''')
              st.write("Given")
              st.latex(r'''
              SA = B + LA       
              ''', help = " Where B = base area, LA = lateral area")
              lsaoctogonal = 8 * octogons * octogonprismh
              octogonsurfacearea = 4 * (1 + mf.sqrt(2)) * (octogons ** 2) + lsaoctogonal
              unitssquared = u'²'
              unitssquaredfull = f''' units {unitssquared} '''
              st.write(f''' The surface area of your prism is {octogonsurfacearea} {unitssquaredfull}''')
       else :
              if prismbaseshape == 9:
                     st.write("Given")
                     st.latex(r'''
                     V = \left(\frac{APh}{2}\right)        
                     ''', help = "Where A = apothem, P = perimeter, and h = prism height.")
                     nonagons = st.number_input("Please enter a side length from the nonagonal base of your prism.")
                     nonagonprismh = st.number_input("Please enter the height of your prism.")
                     vnonagon = ((9 * nonagons ** 2 / 4) * (1 / (mf.tan(3.1415/9)))) * nonagonprismh
                     unitscubed = u'³'
                     unitscubedfull = f''' units {unitscubed} '''
                     st.write(f''' The volume of your octogonal prism is {vnonagon} {unitscubedfull}''')
                     st.write("Given")
                     st.latex(r'''
                     SA = B + LA       
                     ''', help = " Where B = base area, LA = lateral area")
                     cotfornonagon = 0.44699510894
                     surfaceareanonagon = ((9 * nonagons * nonagonprismh) + (9 / 2) * (nonagons ** 2) * (1/(mf.tan(20)))) * 1.94
                     unitssquared = u'²'
                     unitssquaredfull = f''' units {unitssquared} '''
                     st.write(f''' The surface area of your prism is {surfaceareanonagon} {unitssquaredfull}''')
else:
       if option == "Pyramid":
                     prismbaseshape = st.number_input("How many sides does the base of your shape have?", min_value=3, max_value=9)
       if prismbaseshape == 3:
              st.write("Given")
              st.latex(r'''
              V = \left(\frac{\left(\frac{1}{2}\right) b h d}{3}\right)   
              ''')
              triangularprismbase = st.number_input("Please enter the length of the base of your triangle-based pyramid.")
              triangularprismheight = st.number_input("Please enter the length of the height of this triangular base.")
              triangularprismrealheight = st.number_input("Please enter the height of your pyramid.")
              oneovertwo = 1 / 2
              volumeoftriangularp = oneovertwo * triangularprismbase * triangularprismheight * triangularprismrealheight
              converttopyramid = volumeoftriangularp / 3
              unitscubed = u'³'
              unitscubedfull = f''' units {unitscubed} '''
              st.write(f''' The volume of your pyramid is {converttopyramid} {unitscubedfull}''')
              st.write("Given")
              st.latex(r'''
              SA = B + \left(\frac{1}{2}\right)  P  l       
              ''', help = "Where B = base area, P = perimeter, and l = slant height")
              slantheight = st.number_input("Please enter the slant height of your pyramid.")
              volumeofbasetriangle = oneovertwo * triangularprismbase * triangularprismheight
              pyramidtriangleperimeter1 = st.number_input("Enter side length 1 of your base.")
              pyramidtriangleperimeter2 = st.number_input("Enter side length 2 of your base.")
              pyramidtriangleperimeter3 = st.number_input("Enter side length 3 of your base.")
              triangleperimeter = pyramidtriangleperimeter1 + pyramidtriangleperimeter2 + pyramidtriangleperimeter3
              surfaceareatriangularpyramid = volumeofbasetriangle + 1/2 * triangleperimeter * slantheight
              unitssquared = u'²'
              unitssquaredfull = f''' units {unitssquared} '''
              st.write(f''' The surface area of your pyramid is {surfaceareatriangularpyramid} {unitssquaredfull}''')
       elif prismbaseshape == 4:
              st.write("Given")
              st.latex(r'''
              V = \left(\frac{lwh}{3}\right)       
              ''')
              regularprismbase = st.number_input("Please enter the length of the base of your pyramid.")
              regularprismheight = st.number_input("Please enter the width of the base of your pyramid.")
              regularprismrealheight = st.number_input("Please enter the height of your pyramid.")
              volumeofregularp = regularprismbase * regularprismheight * regularprismrealheight
              converttopyramid = volumeofregularp / 3
              unitscubed = u'³'
              unitscubedfull = f''' units {unitscubed} '''
              st.write(f''' The volume of your pyramid is {converttopyramid} {unitscubedfull}''')
              st.write("Given")
              st.latex(r'''
              SA = B + \left(\frac{1}{2}\right)  P  l       
              ''', help = "Where B = base area, P = perimeter, and l = slant height")
              slantheight = st.number_input("Please enter the slant height of your pyramid.")
              basevolume = regularprismbase * regularprismheight
              rectangleperimeter = 2 * regularprismbase + 2 * regularprismheight
              surfacearearegularpyramid = basevolume + 1/2 * rectangleperimeter * slantheight
              unitssquared = u'²'
              unitssquaredfull = f''' units {unitssquared} '''
              st.write(f''' The surface area of your pyramid is {surfacearearegularpyramid} {unitssquaredfull}''')
       elif prismbaseshape == 5:
              st.write("Given")
              st.latex(r'''
              V = \left(\frac{\left(\frac{1}{2}\right) (e1 + e2)  h l}{3}\right)        
              ''', help = "Where e1 and e2 are the two base lengths of the trapezoid base.")
              trapezoidbaseedgeone = st.number_input("Please enter one of the side lengths of your trapezoid base.")
              trapezoidbaseedgetwo = st.number_input("Please enter the other edge length of your trapezoid")
              trapezoidbaseheight = st.number_input("Please enter the height of your trapezoid base.")
              trapezoidprismheight = st.number_input("Please enter the height of your pyramid")
              oneovertwo = 1 / 2
              trapezoidapethom = trapezoidbaseedgeone + trapezoidbaseedgetwo
              trapezoidv = oneovertwo * trapezoidapethom * trapezoidbaseheight * trapezoidprismheight
              converttopyramid = trapezoidv / 3
              unitscubed = u'³'
              unitscubedfull = f''' units {unitscubed} '''
              st.write(f''' The volume of your pyramid is {converttopyramid} {unitscubedfull}''')
              st.write("Given")
              st.latex(r'''
              SA = B + \left(\frac{1}{2}\right)  P  l       
              ''', help = "Where B = base area, P = perimeter, and l = slant height")
              slantheight = st.number_input("Please enter the slant height of your pyramid.")
              basevolume = oneovertwo * trapezoidapethom * trapezoidbaseheight
              sidelength1 = st.number_input("Please enter one of the other two side lengths of your trapezoid base.")
              sidelength2 = st.number_input("Please enter the final side length of your trapezoid base.")
              trapezoidperimeter = trapezoidbaseedgeone + trapezoidbaseedgetwo + sidelength1 + sidelength2 
              surfacearearegularpyramid = basevolume + 1/2 * trapezoidperimeter * slantheight
              unitssquared = u'²'
              unitssquaredfull = f''' units {unitssquared} '''
              st.write(f''' The surface area of your pyramid is {surfacearearegularpyramid} {unitssquaredfull}''')
       elif prismbaseshape == 6:
              st.write("Given")
              st.latex(r'''
              V = \left(\frac{\left(\frac{APh}{2}\right)}{3}\right)     
              ''', help = "Where A = apothem, P = perimeter, and h = prism height.")
              slengthhex = st.number_input("Please enter a side length of your hexagonal base.")
              hexpheight = st.number_input("Pleae enter the height of your pyramid.")
              squarerootthree = mf.sqrt(3)
              productsqrthex = squarerootthree * 3
              quotientsqrthex = productsqrthex / 2
              slsquaredhex = slengthhex ** 2 
              vhexagon = quotientsqrthex * slsquaredhex * hexpheight
              converttopyramid = vhexagon / 3
              unitscubed = u'³'
              unitscubedfull = f''' units {unitscubed} '''
              st.write(f''' The volume of your pyramid is {converttopyramid} {unitscubedfull}''')
              st.write("Given")
              st.latex(r'''
              SA = B + \left(\frac{1}{2}\right)  P  l       
              ''', help = "Where B = base area, P = perimeter, and l = slant height")
              slantheight = st.number_input("Please enter the slant height of your pyramid.")
              vhexagonbase = quotientsqrthex * slsquaredhex
              perimeterhex = 6 * slengthhex
              surfaceareahexagonalpyramid = vhexagonbase + 1/2 * perimeterhex * slantheight
              unitssquared = u'²'
              unitssquaredfull = f''' units {unitssquared} '''
              st.write(f''' The surface area of your pyramid is {surfaceareahexagonalpyramid} {unitssquaredfull}''')              
       elif prismbaseshape == 7:
              st.write("Given")
              st.latex(r'''
              V = \left(\frac{\left(\frac{APh}{2}\right)}{3}\right)       
              ''', help = "Where A = apothem, P = perimeter, and h = prism height.")
              septogons = st.number_input("Please enter a side length for your heptogon.")
              septogonprismheight = st.number_input("Please enter the height of your pyramid.")
              vheptogon = ((7 * septogons ** 2 / 4) * (1 / (mf.tan(3.1415/7)))) * septogonprismheight
              converttopyramid = vheptogon /3
              unitscubed = u'³'
              unitscubedfull = f''' units {unitscubed} '''
              st.write(f''' The volume of your pyramid is {converttopyramid} {unitscubedfull}''')
              vheptogonbase = ((7 * septogons ** 2 / 4) * (1 / (mf.tan(3.1415/7))))
              st.write("Given")
              st.latex(r'''
              SA = B + \left(\frac{1}{2}\right)  P  l       
              ''', help = "Where B = base area, P = perimeter, and l = slant height")
              heptogonperimeter = 7 * septogons
              slantheight = st.number_input("Please enter the slantheight of your pyramid.")
              surfaceareaheptogonpyramid = vheptogonbase + 1/2 * heptogonperimeter * slantheight
              unitssquared = u'²'
              unitssquaredfull = f''' units {unitssquared} '''
              st.write(f''' The surface area of your pyramid is {surfaceareaheptogonpyramid} {unitssquaredfull}''')                 
       elif prismbaseshape == 8:
              st.write("Given")
              st.latex(r'''
              V = \left(\frac{\left(\frac{APh}{2}\right)}{3}\right)      
              ''', help = "Where A = apothem, P = perimeter, and h = prism height.")
              octogons = st.number_input("Please enter a side length from your octogonal base.")
              octogonprismh = st.number_input("Please enter the height of your pyramid.")
              sqrtoctoapothem = 1 + mf.sqrt(2)
              voctogon = 2 * sqrtoctoapothem * octogons ** 2
              voctogonprism = voctogon * octogonprismh
              converttopyramid = voctogonprism / 3
              unitscubed = u'³'
              unitscubedfull = f''' units {unitscubed} '''
              st.write(f''' The volume of your pyramid is {converttopyramid} {unitscubedfull}''')
              st.write("Given")
              st.latex(r'''
              SA = B + \left(\frac{1}{2}\right)  P  l       
              ''', help = "Where B = base area, P = perimeter, and l = slant height")
              slantheight = st.number_input("Please enter the slant height of your pyramid.")
              octogonperimeter = octogons * 8
              surfaceareaoctogonpyramid = voctogon + 1/2 * octogonperimeter * slantheight
              unitssquared = u'²'
              unitssquaredfull = f''' units {unitssquared} '''
              st.write(f''' The surface area of your pyramid is {surfaceareaoctogonpyramid} {unitssquaredfull}''') 
       else :
              if prismbaseshape == 9:
                     st.write("Given")
                     st.latex(r'''
                     V = \left(\frac{\left(\frac{APh}{2}\right)}{3}\right)       
                     ''', help = "Where A = apothem, P = perimeter, and h = prism height.")
                     nonagons = st.number_input("Please enter a side length from the nonagonal base of your pyramid.")
                     nonagonprismh = st.number_input("Please enter the height of your pyramid.")
                     vnonagon = ((9 * nonagons ** 2 / 4) * (1 / (mf.tan(3.1415/9)))) * nonagonprismh
                     converttopyramid = vnonagon / 3
                     unitscubed = u'³'
                     unitscubedfull = f''' units {unitscubed} '''
                     st.write(f''' The volume of your pyramid is {converttopyramid} {unitscubedfull}''')
                     st.write("Given")
                     st.latex(r'''
                     SA = B + \left(\frac{1}{2}\right)  P  l       
                     ''', help = "Where B = base area, P = perimeter, and l = slant height")
                     slantheight = st.number_input("Please enter the slant height of your pyramid.")
                     nonagonperimeter = nonagons * 9
                     vnonagonbase = ((9 * nonagons ** 2 / 4) * (1 / (mf.tan(3.1415/9))))
                     surfaceareanonagonpyramid = vnonagonbase + 1/2 * nonagonperimeter * slantheight
                     unitssquared = u'²'
                     unitssquaredfull = f''' units {unitssquared} '''
                     st.write(f''' The surface area of your pyramid is {surfaceareanonagonpyramid} {unitssquaredfull}''') 

# Begin calculator 2: Pythagorean theorem

st.header("Pythagorean Thereom Calculator")
st.warning("Determine the length of the hypoteneuse of a right-angled triangle with two other sides.")
st.write("Given")
st.latex(r'''
a^2 + b^2 = c^2      
''', help = "Where a and b are determined sides, and c is the hypoteneuse.")
side1pythag = st.number_input("Please enter one of your side lengths.")
side2pythag = st.number_input("Please enter your other side length.")
squaredside1pythag = side1pythag ** 2
squaredside2pythag = side2pythag ** 2
finalpythag = mf.sqrt(squaredside1pythag + squaredside2pythag)
st.write(f''' The hypoteneuse of your triangle is {finalpythag} units''')
