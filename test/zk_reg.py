# -*- coding: utf-8 -*-

import time
from pydubbo.pydubbo import DubboZK
import json

if __name__ == '__main__':
    #d = DubboZK(interface="com.setsuna.api.service.AuthService", hosts='10.7.8.12:2181')
    #d.registry(port=20880,service="com.setsuna.api.service.AuthService2",methods=["hello"],zks="10.7.8.12:2181")
    
    #res = d.authUser([("Ljava/lang/String;", u"workflow"),("Ljava/lang/String;", u"WDz7DYagHx9u")]) #根据返回的方法，动态添加.输入的参数只有一个java string类型
    #token = res.result
    #print("token is : %s"%token)
    #f = DubboZK(interface="com.mryx.moa.bpm.api.service.TicketRpcService", hosts='10.2.39.16:2181',version="1.0.0")
    #f = DubboZK(interface="com.setsuna.api.service.TicketService", hosts='10.7.8.12:2181')
    #f.attachments["access-token"] = token
    
    e = DubboZK(interface="com.mryx.ehr.data.manager.api.DataManagerRpcService", hosts='10.2.39.16:2181')
    data = e.getPersonJobInfoByCondition([("Lcom/mryx/ehr/data/manager/model/request/job/PersonJobQueryReq;",{"userKey":"9SQHzwYdrRuSGSDXCodfOA==","confCode":"moa_person","jobFunction":"105"})])
    
    #int 类型使用标记 I
    #data = f.findTicketByTicketId([("I",6091)]) 
    print(data)