require 'net/http'
require 'json'

module Queries
  class CalculationQuery
    def initialize(seed)
      @seed = seed
    end

    def f(n)
      if n == 0
        1
      elsif n == 2
        2
      elsif n % 2 == 0
        f(n - 1) + f(n - 2) + f(n - 3) + f(n - 4)
      else
        ask_server(n)
      end
    end

    private

    attr_reader :seed

    def uri
      @uri ||= URI.parse(ENV['CALCULATION_API'])
    end

    def ask_server(n)
      params    = { seed:, n: }
      uri.query = URI.encode_www_form(params)
      req       = Net::HTTP::Get.new(uri)
      res       = Net::HTTP.start(uri.host, uri.port) {|http| http.request(req) }
      result    = JSON.parse(res.body)['result']
    end
  end
end
