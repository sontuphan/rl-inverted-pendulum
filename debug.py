import numpy as np

w = np.array(
    [
        [3.28991711e-1, -1.23524226e-1, 1.34562656e-1, -1.48207158e-1, -8.37353244e-2],
        [-1.81893453e-1, -5.77954482e-3, -
            7.67464116e-2, -1.27138883e-1, 3.24876487e-1],
        [-1.23926856e-1, -1.95804045e-1, 2.19271466e-1, -1.75033182e-1, 1.12914562e-1],
        [2.46053953e-2, 7.64220953e-2, -2.10972831e-1, -2.39015102e-1, -1.04738526e-1],
        [-8.9987278e-2, 2.5080506e-5, -1.25605851e-1, -1.24240361e-1, 3.02757204e-1],
        [-1.87092185e-1, 1.87311769e-1, -2.06823766e-1, -2.87815422e-1, 1.78287715e-1],
        [1.45063519e-1, 4.6811223e-2, 1.44875288e-1, -1.46921903e-1, 1.13067538e-1],
        [6.412334e-2, 8.19918886e-2, -2.16775626e-1, -1.77094623e-1, 8.24495479e-2],
        [4.04497981e-2, 8.75213742e-2, -1.96942091e-2, -1.5843587e-2, 8.12182426e-2],
        [-1.65683255e-2, -1.28649145e-1, -1.59585267e-1, 4.93729226e-2, 1.650493e-1],
        [-2.58108646e-1, 1.61903471e-1, -3.84967439e-2, 1.21740572e-1, 2.21852273e-1],
        [-2.46399179e-1, 1.6533792e-1, -8.43370408e-2, -2.02517599e-1, 1.48392901e-1],
        [-1.51444584e-1, -5.26286513e-2, -
            9.0282321e-2, -6.03314489e-2, 8.44613984e-2],
        [-5.07014878e-2, -1.18684597e-1, 4.54381593e-2, -9.23406184e-2, 4.0827807e-2],
        [-1.94042996e-1, -2.41387039e-1, 1.94653198e-1, 4.24177572e-2, 1.80932537e-1],
        [-1.40003979e-1, 5.29020801e-2, 9.4726719e-2, 2.88175941e-1, -2.2102569e-1],
        [-1.01050876e-1, -3.0208556e-2, 1.28461406e-1, 1.81167796e-1, 2.83481032e-1],
        [-7.17308819e-2, -1.73888914e-2, -
            1.98800087e-1, -2.06224427e-1, 2.40695477e-2],
        [-1.30681112e-1, 2.383429e-2, -2.57459998e-1, -1.65277913e-1, -1.5981324e-1],
        [2.05666453e-1, 3.47043835e-2, 7.38301501e-2, -9.1056101e-2, -1.07093059e-1],
        [-2.55241692e-2, -2.14318171e-1, -
            2.30104282e-1, -4.87091765e-2, -2.88311779e-1],
        [1.89409032e-1, 2.75614172e-1, -1.37818664e-1, 3.03015292e-1, 5.71666919e-2],
        [1.11470766e-1, -1.44538552e-1, 2.54517317e-1, 2.92146742e-1, 2.13990986e-1],
        [9.94221345e-2, 2.1172744e-1, -2.29228005e-1, -1.47973865e-1, -1.04878187e-1],
        [3.13969739e-2, 1.96043462e-1, -1.33773908e-1, -2.84891456e-1, 1.24699011e-1],
        [-4.38518673e-1, -1.41861528e-1, 2.13824987e-1, -1.1554119e-1, -4.52793948e-2],
        [2.25048184e-1, -5.4099462e-3, 1.4627102e-1, 9.4776243e-2, -1.74687266e-1],
        [-8.95351346e-4, -8.6157687e-2, 2.26816773e-1, 3.83119769e-2, -1.6779542e-1],
        [3.53692383e-1, 1.54928952e-1, 5.28120156e-3, 1.42661586e-1, -7.85627291e-2],
        [1.84001625e-1, -2.8594967e-2, 2.51954228e-1, 1.83921039e-1, -1.36850595e-1],
        [1.30623862e-1, -1.04540601e-1, -2.1576187e-1, -3.72512966e-1, -4.25198883e-1],
        [3.53750214e-2, -1.07677519e-1, 4.38115597e-2, -1.50530832e-2, -2.25575313e-1],
        [9.63223819e-3, -1.583471e-1, -1.30844116e-1, -6.57670666e-3, 2.67065465e-1],
        [2.34665766e-1, 3.35674435e-1, 2.05407545e-1, 3.64094406e-1, 1.242553e-1],
        [5.294168e-2, -2.71038294e-1, 8.47700238e-2, 1.92283943e-1, 2.33702958e-1],
        [6.81896554e-3, 2.93622017e-1, 7.74423257e-2, -4.99638543e-2, 8.97985399e-2],
        [6.72188178e-2, -2.80228347e-1, 1.77516416e-1, -5.75411096e-2, 2.09734097e-1],
        [1.71026573e-1, 2.82222271e-1, 9.86056216e-3, 2.1627536e-2, 2.6106444e-1],
        [-2.34790027e-1, 7.64277577e-2, 1.02593027e-1,
            8.74802247e-2, -2.03773469e-1],
        [-1.0665261e-1, -6.62992746e-2, -
            2.63365686e-1, -2.18316153e-1, -2.26994649e-1],
        [1.90930814e-1, 2.13510111e-1, 2.53753126e-1, 1.3812995e-1, 1.80324063e-1],
        [-1.38402179e-1, 1.23755179e-1, 1.57123625e-1, -1.68688178e-1, -1.46224603e-1],
        [2.82350451e-1, 7.71471262e-2, -9.26044658e-2, 2.1472697e-1, 1.00577027e-1],
        [-1.86415523e-1, 2.61855394e-1, -1.33267464e-2, -1.44098327e-1, -4.3336153e-2],
        [5.01251407e-2, 7.4066571e-3, 7.41044506e-2, 5.80303185e-2, 1.35297686e-1],
        [-7.86458403e-2, -1.25691906e-1, 3.26537073e-1, 1.62052244e-1, 2.44366616e-1],
        [3.21361661e-1, 9.65624582e-3, -2.62180179e-1, -1.56664282e-1, -6.02418333e-2],
        [-3.85817468e-1, 1.46994106e-2, -7.84860551e-2, 1.47249714e-1, 1.51099607e-1],
        [-2.04148561e-1, 9.70501378e-2, -1.7370607e-1, -1.24605827e-1, 3.42563055e-2],
        [2.48192638e-1, 1.58433735e-1, -1.65427953e-1, 6.04774393e-2, 4.4596456e-2],
        [-4.70911153e-2, -3.24005008e-1, -
            1.32329971e-1, -2.59548664e-1, -2.88545161e-1],
        [-2.95416892e-1, 5.65205002e-3, -1.81303874e-1, 1.24475501e-1, 1.03375003e-1],
        [-4.50708233e-2, -8.32142159e-2, 1.28388584e-1,
            2.63564348e-1, -3.30806196e-1],
        [-1.14782169e-1, 2.4255538e-1, 1.51345076e-3, 1.30841881e-2, 4.72632051e-3],
        [2.14026153e-1, -1.06270209e-1, -2.16995571e-2, 1.45492524e-1, 1.31675586e-1],
        [1.00854695e-1, 9.92833897e-2, -2.71551073e-1, -2.0457698e-2, 2.83436447e-1],
        [-6.19351789e-2, 1.65802017e-1, -
            2.21792057e-1, -2.30602905e-1, -1.03475928e-1],
        [1.1065916e-1, 2.93418139e-1, 9.15071219e-2, 3.4494856e-1, 9.22103748e-2],
        [4.40620333e-2, -4.77664508e-2, -1.02820143e-1, -1.98686957e-1, 1.18580222e-1],
        [1.2465404e-1, 2.55692482e-1, -8.4828876e-2, 1.43582791e-1, 8.45968202e-2],
        [5.43564782e-2, 1.14270777e-1, 3.08472723e-1, 1.70933425e-1, 3.94191772e-1],
        [-1.21791899e-1, 1.42413005e-1, 2.20929161e-1, 2.05455651e-3, 1.06126875e-1],
        [-2.30975091e-1, 1.55511931e-1, -2.75627851e-1, -1.4075987e-1, 6.96054995e-2],
        [-1.02846146e-1, 6.251885e-2, -1.94614485e-1, 8.71217251e-2, 2.35042214e-1]
    ]
)

b = np.array([[-1.9272127, -2.0987492, -1.9184209, -2.1942587, -0.4241627]])

l1 = np.array([[0.06041846, 0, 0.1342541, 0, 0, 0.0996584,
                0.03575344, 0, 0.03590255, 0, 0, 0.02664652,
                0, 0, 0, 0.15752417, 0, 0,
                0, 0.06952064, 0, 0.12556146, 0.1914795, 0,
                0.09690088, 0.09631908, 0, 0, 0.19129989, 0.04185006,
                0.03898828, 0.08562341, 0, 0.24578379, 0, 0,
                0.20834428, 0, 0.08428789, 0, 0.13149919, 0.0638323,
                0, 0, 0.05395197, 0.08849926, 0, 0,
                0.02515115, 0, 0.00512419, 0, 0.06931692, 0.2998701,
                0.00487732, 0.10574362, 0.02836782, 0.02542898, 0, 0,
                0, 0, 0.22341089, 0]])

r = np.matmul(l1, w) + b
print(r)
