REGION=-2.5 2.5 -2.5 2.5 
GRID=0.05 0.05
HIGH=250000
LOW=50000
ORDER_LOW= 2 2 2
ORDER_HIGH= 10 10 10
TESSGRAV_PATH=/home/leo/src/tesseroids/trunk/python/
MODEL_FILE=model.txt

all: gxx gxy gxz gyy gyz gzz


gxx: gxx-250-o2.dat gxx-50-o2.dat gxx-50-o10.dat


gxx-250-o2.dat: ${MODEL_FILE}
	${TESSGRAV_PATH}tessgxx $< -r ${REGION} -b ${GRID} -o ${ORDER_LOW} -e ${HIGH} > $@


gxx-50-o2.dat: ${MODEL_FILE}
	${TESSGRAV_PATH}tessgxx $< -r ${REGION} -b ${GRID} -o ${ORDER_LOW} -e ${LOW} > $@


gxx-50-o10.dat: ${MODEL_FILE}
	${TESSGRAV_PATH}tessgxx $< -r ${REGION} -b ${GRID} -o ${ORDER_HIGH} -e ${LOW} > $@


gxy: gxy-250-o2.dat gxy-50-o2.dat gxy-50-o10.dat


gxy-250-o2.dat: ${MODEL_FILE}
	${TESSGRAV_PATH}tessgxy $< -r ${REGION} -b ${GRID} -o ${ORDER_LOW} -e ${HIGH} > $@


gxy-50-o2.dat: ${MODEL_FILE}
	${TESSGRAV_PATH}tessgxy $< -r ${REGION} -b ${GRID} -o ${ORDER_LOW} -e ${LOW} > $@


gxy-50-o10.dat: ${MODEL_FILE}
	${TESSGRAV_PATH}tessgxy $< -r ${REGION} -b ${GRID} -o ${ORDER_HIGH} -e ${LOW} > $@


gxz: gxz-250-o2.dat gxz-50-o2.dat gxz-50-o10.dat


gxz-250-o2.dat: ${MODEL_FILE}
	${TESSGRAV_PATH}tessgxz $< -r ${REGION} -b ${GRID} -o ${ORDER_LOW} -e ${HIGH} > $@


gxz-50-o2.dat: ${MODEL_FILE}
	${TESSGRAV_PATH}tessgxz $< -r ${REGION} -b ${GRID} -o ${ORDER_LOW} -e ${LOW} > $@


gxz-50-o10.dat: ${MODEL_FILE}
	${TESSGRAV_PATH}tessgxz $< -r ${REGION} -b ${GRID} -o ${ORDER_HIGH} -e ${LOW} > $@


gyy: gyy-250-o2.dat gyy-50-o2.dat gyy-50-o10.dat


gyy-250-o2.dat: ${MODEL_FILE}
	${TESSGRAV_PATH}tessgyy $< -r ${REGION} -b ${GRID} -o ${ORDER_LOW} -e ${HIGH} > $@


gyy-50-o2.dat: ${MODEL_FILE}
	${TESSGRAV_PATH}tessgyy $< -r ${REGION} -b ${GRID} -o ${ORDER_LOW} -e ${LOW} > $@


gyy-50-o10.dat: ${MODEL_FILE}
	${TESSGRAV_PATH}tessgyy $< -r ${REGION} -b ${GRID} -o ${ORDER_HIGH} -e ${LOW} > $@


gyz: gyz-250-o2.dat gyz-50-o2.dat gyz-50-o10.dat


gyz-250-o2.dat: ${MODEL_FILE}
	${TESSGRAV_PATH}tessgyz $< -r ${REGION} -b ${GRID} -o ${ORDER_LOW} -e ${HIGH} > $@


gyz-50-o2.dat: ${MODEL_FILE}
	${TESSGRAV_PATH}tessgyz $< -r ${REGION} -b ${GRID} -o ${ORDER_LOW} -e ${LOW} > $@


gyz-50-o10.dat: ${MODEL_FILE}
	${TESSGRAV_PATH}tessgyz $< -r ${REGION} -b ${GRID} -o ${ORDER_HIGH} -e ${LOW} > $@


gzz: gzz-250-o2.dat gzz-50-o2.dat gzz-50-o10.dat


gzz-250-o2.dat: ${MODEL_FILE}
	${TESSGRAV_PATH}tessgzz $< -r ${REGION} -b ${GRID} -o ${ORDER_LOW} -e ${HIGH} > $@


gzz-50-o2.dat: ${MODEL_FILE}
	${TESSGRAV_PATH}tessgzz $< -r ${REGION} -b ${GRID} -o ${ORDER_LOW} -e ${LOW} > $@


gzz-50-o10.dat: ${MODEL_FILE}
	${TESSGRAV_PATH}tessgzz $< -r ${REGION} -b ${GRID} -o ${ORDER_HIGH} -e ${LOW} > $@


clean:
	rm g*.dat
